import json
from datetime import datetime
from utils.post_utils import (
    read_posts,
    write_posts,
    generate_post_id,
    get_current_datetime,
)
from utils.auth_utils import current_user  # چون از current_user هم استفاده کردی


DATA_FILE = "posts.json"


def load():
    return read_posts()


def save_posts(posts):
    write_posts(posts)


def generate_post_id(posts):
    return max([p["id"] for p in posts], default=0) + 1


def add_post(title, content, author):
    posts = load()
    post_id = generate_post_id(posts)
    post = {
        "id": post_id,
        "title": title,
        "content": content,
        "author": author,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "likes": [],
        "comments": [],
    }
    posts.append(post)
    save_posts(posts)
    print(f"✅ Post '{title}' added successfully with ID {post_id}.")


def show_posts(posts):
    posts = [p for p in posts if "created_at" in p]
    posts = sorted(posts, key=lambda x: x["created_at"], reverse=True)
    for post in posts:
        print(f"\n🆔 ID: {post['id']}")
        print(f"📌 Title: {post['title']}")
        print(f"📝 Content: {post['content']}")
        print(f"👤 Author: {post['author']}")
        print(f"📅 Created: {post['created_at']}")
        print(f"🕓 Updated: {post['updated_at']}")
        print(f"❤️ Likes: {len(post['likes'])}")
        print(f"💬 Comments: {len(post['comments'])}")
        print("-" * 40)


def show_post_details(post_id):
    posts = load()
    for post in posts:
        if post["id"] == post_id:
            print(f"\n📌 Title: {post['title']}")
            print(f"👤 Author: {post['author']}")
            print(f"📅 Date: {post['created_at']}")
            print(f"❤️ Likes: {len(post['likes'])}")
            print(f"\n--- {post['content']}\n")

            print("💬 Comments:")
            for c in post["comments"]:
                print(f" - {c['user']} ({c['date']}): {c['text']}")
            return
    print("❌ Post not found.")


def search_posts(query):
    posts = load()
    results = [
        p
        for p in posts
        if query.lower() in p["title"].lower() or query.lower() in p["content"].lower()
    ]
    if results:
        show_posts(results)
    else:
        print("❌ No posts found matching your search.")


def edit_post(post_id, new_title, new_content):
    posts = load()
    for post in posts:
        if post["id"] == post_id and post["author"] == current_user:
            post["title"] = new_title
            post["content"] = new_content
            post["updated_at"] = datetime.now().isoformat()
            save_posts(posts)
            print(f"✅ Post ID {post_id} updated successfully.")
            return
    print("❌ Post not found or you don't have permission to edit.")


def delete_post(post_id):
    posts = load()
    for post in posts:
        if post["id"] == post_id and post["author"] == current_user:
            posts.remove(post)
            save_posts(posts)
            print(f"🗑️ Post ID {post_id} deleted successfully.")
            return
    print("❌ Post not found or you don't have permission to delete.")


def like_post(post_id):
    posts = load()
    for post in posts:
        if post["id"] == post_id:
            if current_user not in post["likes"]:
                post["likes"].append(current_user)
                save_posts(posts)
                print(f"👍 Post ID {post_id} liked successfully.")
            else:
                print("⚠️ You already liked this post.")
            return
    print("❌ Post not found.")


def comment_on_post(post_id, comment_text):
    posts = load()
    for post in posts:
        if post["id"] == post_id:
            comment = {
                "user": current_user,
                "text": comment_text,
                "date": datetime.now().isoformat(),
            }
            post["comments"].append(comment)
            save_posts(posts)
            print(f"💬 Comment added to Post ID {post_id}.")
            return
    print("❌ Post not found.")


def view_comments(post_id):
    posts = load()
    for post in posts:
        if post["id"] == post_id:
            if post["comments"]:
                print(f"💬 Comments for Post ID {post_id}:")
                for comment in post["comments"]:
                    print(f"{comment['user']} ({comment['date']}): {comment['text']}")
            else:
                print("🛑 No comments yet.")
            return
    print("❌ Post not found.")


def show_user_posts(username):
    posts = load()
    user_posts = [p for p in posts if p["author"] == username]
    if user_posts:
        show_posts(user_posts)
    else:
        print("❌ No posts found for this user.")


def show_all_posts():
    posts = load()
    if posts:
        show_posts(posts)
    else:
        print("📭 No posts available.")


def show_my_posts():
    posts = load()
    user_posts = [p for p in posts if p["author"] == current_user]
    if user_posts:
        show_posts(user_posts)
    else:
        print("❌ You have not written any posts yet.")
    return user_posts
