import csv
import os
from flask import render_template


PATH_TO_CITY = "/home/abc/Downloads/city_name.csv"
PATH_TO_SAVE_USER = "/home/abc/Downloads/user_profiles.csv"


def dropdown_options():
    cities = []

    with open(PATH_TO_CITY, newline= "") as cities_data:
        reader = csv.DictReader(cities_data)

        for row in reader:
            cities.append({'id': row['id'], 'name': row['name']})

        return cities


def save_to_csv(new_data):
    if not os.path.isfile(PATH_TO_SAVE_USER):
        with open(PATH_TO_SAVE_USER, mode='w', newline="") as user_data:
            field_names = ['id', 'name']
            writer = csv.DictWriter(user_data, fieldnames = field_names)
            writer.writeheader()
            writer.writerow(new_data)
    else:
        with open(PATH_TO_SAVE_USER, mode='a', newline="") as user_data:
            field_names = ['id', 'name']
            writer = csv.DictWriter(user_data, fieldnames= field_names)
            writer.writerow(new_data)

    user_data.close()

    return render_template("success.html")