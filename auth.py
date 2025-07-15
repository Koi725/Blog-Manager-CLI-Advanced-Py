from utils import init, read_data, write_data
from passwordChecker import check_password_strength
import re


def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    data = read_data()

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            print(f"Logged in successfully! Welcome {username}!")
            return 1
    print("Incorrect username or password.")
    return 0


def signup():
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format. Please try again.")
        return 0
    password = input("Please enter your password: ")

    score = int(check_password_strength(password))

    if score < 6:
        print("Password is too weak. Please choose a stronger password.")
        return
    else:
        data = read_data()
        for user in data["users"]:
            if user["username"] == username:
                print("Username already exists. Please try a different one.")
                return 0
        data["users"].append(
            {"username": username, "password": password, "email": email}
        )
        write_data(data)
        print("Sign-up successful! You can now log in.")
    return 1
