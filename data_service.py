import json
import os

from global_constants import *


def get_all_data():
    data = []
    with open(os.path.join(DB_FOLDER_NAME, DATA_FILE), 'r') as file:
        for line in file:
            data.append(json.loads(line.strip()))
        return data

def get_employer_data():
    employer_data = []
    with open(os.path.join(DB_FOLDER_NAME, EMPLOYER_DATA_FILE), 'r') as file:
        for line in file:
            employer_data.append(json.loads(line.strip()))
        return employer_data
