import requests

# Configuration - update these with your own details
INSTANCE_URL = "https://mastodon.social"  # Replace with your Mastodon instance URL
ACCESS_TOKEN = "czv008jsZ9gWNi3nNFoL9F_3R0oUlYjWI4kYuBDm1tk"        # Replace with your OAuth access token

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def read_home_timeline(limit=5, verbose=False):
    """
    Fetches and displays the latest statuses from the home timeline.
    In verbose mode, prints additional metadata for each status.
    """
    url = f"{INSTANCE_URL}/api/v1/timelines/home?limit={limit}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        timeline = response.json()
        print("\n--- Home Timeline ---\n")
        for status in timeline:
            account = status.get("account", {})
            display_name = account.get("display_name") or account.get("username")
            acct = account.get("acct")
            created_at = status.get("created_at")
            status_id = status.get("id")
            visibility = status.get("visibility")
            sensitive = status.get("sensitive")
            spoiler_text = status.get("spoiler_text")
            content = status.get("content")
            replies_count = status.get("replies_count")
            reblogs_count = status.get("reblogs_count")
            favourites_count = status.get("favourites_count")
            
            # Basic output
            print(f"ID: {status_id}")
            print(f"Account: {display_name} (@{acct})")
            
            # Verbose mode outputs additional metadata
            if verbose:
                print(f"Created at: {created_at}")
                print(f"Visibility: {visibility}")
                print(f"Sensitive: {sensitive}")
                if spoiler_text:
                    print(f"Spoiler Text: {spoiler_text}")
                print(f"Replies: {replies_count} | Reblogs: {reblogs_count} | Favourites: {favourites_count}")
            
            print("Content:")
            print(content)
            print("-" * 50)
    else:
        print("Failed to fetch timeline:")
        print(f"Status Code: {response.status_code}")
        print(response.text)

def post_status(status_text):
    """
    Posts a new status (toot) to Mastodon.
    """
    url = f"{INSTANCE_URL}/api/v1/statuses"
    data = {
        "status": status_text
    }
    response = requests.post(url, headers=HEADERS, data=data)
    
    if response.status_code == 200:
        print("Status posted successfully!")
    else:
        print("Failed to post status:")
        print(f"Status Code: {response.status_code}")
        print(response.text)

def main():
    print("Fetching your home timeline...")
    # Toggle verbose mode by setting verbose=True
    read_home_timeline(limit=5, verbose=True)
    
    choice = input("Would you like to post a new status? (y/n): ").strip().lower()
    if choice == "y":
        status_text = "input("Enter your status: ")"
        post_status(status_text)
    else:
        print("Exiting without posting.")

if __name__ == "__main__":
    main()
