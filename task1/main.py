from datetime import datetime
import random
import re


def get_days_from_today(date_name):
    try:
        new_number = datetime.today() - datetime.strptime(date_name, "%Y-%m-%d")
        return int(new_number.days)
    except ValueError as e:
        print("Incorrect date format. Please enter YYYY-MM-DD")
        return e