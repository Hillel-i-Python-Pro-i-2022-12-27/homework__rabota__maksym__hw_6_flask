from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args
from application.astronauts.amount_of_astronauts import astronauts
from application.average.avarage_params import average_params
from application.users_generator.users_generator import generate_users
from application.get_content.read_file import actions_with_file
app = Flask(__name__)


@app.route("/")
def hello():  # put application's code here
    return (
        "<h1>WELCOME TO HOME PAGE!</h1>"
        "<p><a href='./get_content'>GET CONTENT</p>"
        "<p><a href='./generate-users'>GENERATE USERS</p>"
        "<p><a href='./space'>SPACE</p>"
        "<p><a href='./mean'>MEAN</p>"
    )


@app.route("/get_content")
def get_content(file=actions_with_file()):
    with open(file) as data:
        content = data.read()
    return f"<h1>GET CONTENT</h1>" f"{content}" f"<br><a href='/'>←BACK</a>"


#@app.route("/generate-users")
#@use_args({"amount": fields.Int(missing=10)}, location="query")
#def generate_users():
   # amount = args("amount")
   # users = generate_users
   # return


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


if __name__ == "__main__":
    app.run()
