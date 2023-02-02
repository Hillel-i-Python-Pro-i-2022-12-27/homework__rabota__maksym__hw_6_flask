import pandas as pd

from application.config.paths import FILES_OUTPUT_PATH


def average_params():
    path_to_file = FILES_OUTPUT_PATH.joinpath("hw.csv")
    df = pd.read_csv(path_to_file)

    avr_height = df["Height(Inches)"].mean()
    cm_height = round(avr_height * 2.54, 3)
    avr_weight = df["Weight(Pounds)"].mean()
    kg_weight = round(avr_weight * 0.45, 3)
    return f"Average height is: {cm_height} cm.\nAverage weight is: {kg_weight} kg."
