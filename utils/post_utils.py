import os
import json
from datetime import datetime

POSTS_FILE = "posts.json"


def init_post_file():
    if not os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "w") as f:
            json.dump({"posts": []}, f, indent=3)


def read_posts():
    init_post_file()
    with open(POSTS_FILE, "r") as f:
        data = json.load(f)
    return data.get("posts", [])


def write_posts(posts):
    with open(POSTS_FILE, "w") as f:
        json.dump({"posts": posts}, f, indent=3)


def generate_post_id(posts):
    return max([p["id"] for p in posts], default=0) + 1


def get_current_datetime():
    return datetime.now().isoformat()
