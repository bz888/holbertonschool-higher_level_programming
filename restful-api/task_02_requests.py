import requests, csv

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    try:
        response = requests.get(POSTS_URL, timeout=10)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(f"Post ID: {post['id']}, Title: {post['title']}")
        else:
            print("Failed to fetch posts.")

    except requests.RequestException as error:
        print(f"An error occurred: {error}")


def fetch_and_save_posts():
    try:
        response = requests.get(POSTS_URL, timeout=10)

        if response.status_code == 200:
            posts = response.json()

            with open("posts.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "title", "body"],
                )
                writer.writeheader()

                for post in posts:
                    writer.writerow({
                        "id": post["id"],
                        "title": post["title"],
                        "body": post["body"],
                    })
        else:
            print("Failed to fetch posts.")

    except requests.RequestException as error:
        print(f"An error occurred: {error}")
