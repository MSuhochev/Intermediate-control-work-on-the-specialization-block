# Input - Output module for saving and reading notes to a JSON file

import os
import json


def save_json(data, file): 
    if len(data) > 0:
        with open(file, 'w', encoding='UTF-8') as f:
            json.dump(data, f)


def load_json(file):  
    if os.path.isfile(file):
        with open(file, 'r', encoding='UTF-8') as f:
            return json.load(f)
    else:
        return []