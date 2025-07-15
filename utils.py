import json
import os

DATA_FILE = "user.json"


def init():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": []}, f)


def read_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data


def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=3)
