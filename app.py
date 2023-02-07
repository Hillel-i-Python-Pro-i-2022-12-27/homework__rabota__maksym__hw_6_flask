from flask import Flask, Response
from webargs import fields
from webargs.flaskparser import use_args

from application.astronauts.amount_of_astronauts import astronauts
from application.average.avarage_params import average_params
from application.get_content.read_file import actions_with_file
from application.services.create_table import create_table
from application.services.db_connection import DBConnection
from application.users_generator.users_generator import users_from_json_file

app = Flask(__name__)


@app.route("/")
def hello():  # put application's code here
    return (
        "<h1>WELCOME TO HOME PAGE!</h1>"
        "<p><a href='./get_content'>GET CONTENT</a></p>"
        "<p><a href='./generate-users'>GENERATE USERS</a></p>"
        "<p><a href='./space'>SPACE</a></p>"
        "<p><a href='./mean'>MEAN</a></p>"
        "<br><h1>URL REQUESTS:</h1>"
        "<li>/contacts/create?contact_name=*input_name*&phone_value=*input_number*  "
        "  >>> create row in phone book by contact_name and phone_value</li>"
        "<li>/contacts/read-all    >>> show all phone book by Primary Key</li>"
        "<li>/contacts/read/<int>    >>> show phone book by Primary Key</li>"
        "<li>/contacts/update/search_key?contact_name=&phone_value=   >>> update phone book row by Primary Key</li>"
        "<li>/contacts/delete/<int>    >>> delete phone book row by Primary Key</li>"
    )


@app.route("/get_content")
def get_content(file=actions_with_file()):
    with open(file) as data:
        content = data.read()
    return f"<h1>GET CONTENT</h1>" f"{content}" f"<br><a href='/'>←BACK</a>"


@app.route("/generate-users")
def generate_users(data=users_from_json_file()):
    content: str = ""
    for users in data:
        content += f"<p>{users['name']} : {users['email']}<p>"
    return f"<h1>GENERATE USERS</h1>" f"{content}" f"<a href='/'>←BACK</a>"


@app.route("/space")
def space(path_to_file=astronauts()):
    file = path_to_file
    text_file = open(file)
    content = text_file.read()
    return f"<h1>SPACE</h1>" f"{content}" f"<br><a href='/'>←BACK</a>"


@app.route("/mean")
def average() -> str:
    avr_height, avr_weight = average_params()
    return (
        f"<h1>MEAN</h1>"
        f"<p>Average HEIGHT is: {avr_height} cm.</p>"
        f"<p>Average WEIGHT is: {avr_weight} kg.</p>"
        f"<a href='/'>←BACK</a>"
    )


@app.route("/contacts/create")
@use_args({"contact_name": fields.Str(required=True), "phone_value": fields.Str(required=True)}, location="query")
def create_contacts(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (:contact_name, :phone_value);",
                {"contact_name": args["contact_name"], "phone_value": args["phone_value"]},
            )
    return "Success!"


@app.route("/contacts/read-all")
def contacts__read__all():
    with DBConnection() as connection:
        table_ = connection.execute("SELECT * FROM phones;").fetchall()
        return "<br>".join([f'{row_["pk"]}. {row_["contact_name"]} - {row_["phone_value"]}' for row_ in table_])


@app.route("/contacts/read/<int:pk>")
def contact__read(pk: int):
    with DBConnection() as connection:
        table_ = connection.execute(
            "SELECT * FROM phones WHERE (pk=:pk);",
            {
                "pk": pk,
            },
        ).fetchone()
    return f'{table_["pk"]}: {table_["contact_name"]} - {table_["phone_value"]}'


@app.route("/contacts/update/<int:pk>")
@use_args({"contact_name": fields.Str(), "phone_value": fields.Str()}, location="query")
def contacts__update(args, pk: int):
    with DBConnection() as connection:
        with connection:
            contact_name = args.get("contact_name")
            phone_value = args.get("phone_value")

            if contact_name is None and phone_value is None:
                return Response("You need to provide any argument to update the contact!", status=400)

            args_for_request = []
            if contact_name is not None:
                args_for_request.append("contact_name=:contact_name")
            if phone_value is not None:
                args_for_request.append("phone_value=:phone_value")
            answer = ", ".join(args_for_request)

            connection.execute(
                "UPDATE phones " f"SET {answer} " "WHERE pk=:pk;",
                {
                    "pk": pk,
                    "contact_name": contact_name,
                    "phone_value": phone_value,
                },
            )
    return "Success!"


@app.route("/contacts/delete/<int:pk>")
def contacts__delete(pk: int):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM phones " "WHERE (pk=:pk);",
                {
                    "pk": pk,
                },
            )
    return "Success!"


create_table()
if __name__ == "__main__":
    app.run()
