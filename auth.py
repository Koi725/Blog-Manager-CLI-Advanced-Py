import re
from passwordChecker import check_password_strength
from utils.auth_utils import *
import utils

DATA_FILE = "user.json"


def login():
    username = input("👤 Enter your username: ").strip()
    password = input("🔒 Enter your password: ")
    data = read_users()

    for user in data["users"]:
        if user["username"].strip() == username and user["password"] == password:
            print(f"✅ Logged in successfully! Welcome, {username}!")
            utils.current_user = username
            return 1
    print("❌ Incorrect username or password.")
    return 0


def signup():
    username = input("👤 Choose a username: ").strip()
    email = input("📧 Enter your email: ").strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("❌ Invalid email format. Please try again.")
        return 0

    password = input("🔒 Choose a strong password: ")
    score = int(check_password_strength(password))

    if score < 6:
        print("❌ Password is too weak. Please choose a stronger password.")
        return 0

    data = read_users()
    for user in data["users"]:
        if user["username"].strip() == username:
            print("⚠️ Username already exists. Please choose a different one.")
            return 0

    data["users"].append({"username": username, "password": password, "email": email})
    write_users(data)
    print("✅ Sign-up successful! You can now log in.")
    return 1
