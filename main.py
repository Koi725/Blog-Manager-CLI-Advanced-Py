from auth import login, signup
from utils import init, read_data, write_data


def Login():
    print(
        """
  ==================== LOGIN ====================
  Please enter your credentials to log in.
  If you don't have an account, please sign up first.
  1- Login
  2- Sign Up
  3- Exit
  ===============================================
  """
    )


def main():
    while True:
        Login()
        try:
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
        if choice == 1:
            login()
        elif choice == 2:
            signup()
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
