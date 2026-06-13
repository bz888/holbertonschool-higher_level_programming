import requests, csv

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    try:
        response = requests.get(POSTS_URL, timeout=10)
        response.raise_for_status()

        print(f"Status Code: {response.status_code}")

        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")

    except requests.RequestException as error:
        print(f"An error occurred: {error}")


def fetch_and_save_posts():
    try:
        response = requests.get(POSTS_URL, timeout=10)
        response.raise_for_status()

        posts = response.json()

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title"])
            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                })

    except requests.RequestException as error:
        print(f"An error occurred: {error}")
