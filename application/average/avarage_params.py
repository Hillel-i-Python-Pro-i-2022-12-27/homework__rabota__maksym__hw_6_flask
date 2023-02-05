import csv

from application.config.paths import FILES_OUTPUT_PATH


def average_params():
    path_to_file = FILES_OUTPUT_PATH.joinpath("hw.csv")
    with open(path_to_file) as csv_file:
        height = 0
        weight = 0
        reader = csv.DictReader(csv_file)

        for row in reader:
            height += float(row["Height(Inches)"])
            weight += float(row["Weight(Pounds)"])

        avr_height = round(float(height / int(row["Index"]) * 2.54), 3)  # cm
        avr_weight = round(float(weight / int(row["Index"]) * 0.45), 3)  # kg
    return avr_height, avr_weight
