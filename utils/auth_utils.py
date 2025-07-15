import os
import json

USER_FILE = "user.json"
current_user = None


def init_user_file():
    """Create user.json if it doesn't exist."""
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({"users": []}, f, indent=3)


def read_users():
    """Read user data from user.json."""
    init_user_file()
    with open(USER_FILE, "r") as f:
        data = json.load(f)
    return data


def write_users(data):
    """Write user data to user.json."""
    with open(USER_FILE, "w") as f:
        json.dump(data, f, indent=3)
