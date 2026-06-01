import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json."""
    try:
        with open(csv_filename, "r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
