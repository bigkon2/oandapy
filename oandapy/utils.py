import os
import csv
import json


def json_to_csv(json_file_path, csv_name, delete_source=False):
    """
    Converts json file to csv.
    :param json_file_path: json file which needs to be converted to csv
    :param csv_name: name for the csv file
    :param delete_source: should json file be deleted or not
    :return: path to new csv file
    """
    with open(json_file_path, 'r') as f:
        data = json.loads(f.read())
    headers = []
    for line in data:
        for key in line.iterkeys():
            if key not in headers:
                headers.append(key)
    csv_file_path = os.path.join(os.path.dirname(json_file_path), csv_name)
    with open(csv_file_path, 'w') as f:
        csv_file = csv.DictWriter(f, headers)
        csv_file.writeheader()
        csv_file.writerows(data)
    if delete_source:
        os.remove(json_file_path)
    return csv_file_path
