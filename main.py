from auth import login, signup
from post_manager import *
from utils.auth_utils import current_user
import utils


def loginMenu():
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


def menu():
    print(
        """
  ==================== MENU ====================  
  1. Add New Post
  2. Show My Posts
  3. Show All Posts
  4. Search Post
  5. Edit Post
  6. Delete Post
  7. Like a Post
  8. Comment on a Post
  9. View Comments
  10. Logout  
  ===============================================
  """
    )


def main():
    while True:
        loginMenu()
        try:
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number (1, 2, or 3).")
            continue

        if choice == 1:
            if login():
                break
        elif choice == 2:
            if signup():
                break
        elif choice == 3:
            print("👋 Exiting the application. Goodbye!")
            return
        else:
            print("❌ Invalid choice. Please try again.")

    # Logged in successfully
    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if choice == 1:
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            add_post(title, content, current_user)

        elif choice == 2:
            print("📃 Showing your posts:")
            show_my_posts()

        elif choice == 3:
            show_all_posts()

        elif choice == 4:
            search_term = input("Enter search term: ")
            search_posts(search_term)

        elif choice == 5:
            try:
                post_id = int(input("Enter post ID to edit: "))
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                edit_post(post_id, new_title, new_content)
            except ValueError:
                print("❌ Invalid post ID. Must be a number.")

        elif choice == 6:
            try:
                post_id = int(input("Enter post ID to delete: "))
                delete_post(post_id)
            except ValueError:
                print("❌ Invalid post ID. Must be a number.")

        elif choice == 7:
            try:
                post_id = int(input("Enter post ID to like: "))
                like_post(post_id)
            except ValueError:
                print("❌ Invalid post ID. Must be a number.")

        elif choice == 8:
            try:
                post_id = int(input("Enter post ID to comment on: "))
                comment_text = input("Enter your comment: ")
                comment_on_post(post_id, comment_text)
            except ValueError:
                print("❌ Invalid post ID. Must be a number.")

        elif choice == 9:
            try:
                post_id = int(input("Enter post ID to view comments: "))
                view_comments(post_id)
            except ValueError:
                print("❌ Invalid post ID. Must be a number.")

        elif choice == 10:
            print("🔓 Logging out...")
            utils.current_user = None
            print("✅ You have been logged out.")
            return

        else:
            print("❌ Invalid choice. Please select a number from 1 to 10.")


if __name__ == "__main__":
    main()
