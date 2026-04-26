import sys 
import requests 

from utils import validate_input, format_event


def fetch_activity(username):
        response = requests.get(f"https://api.github.com/users/{username}/events")
        response.raise_for_status()
        return response


def main():
    # Get and validate user input 
    user_input = sys.argv[1:]
    if validate_input(user_input):
        username = user_input[0]
    else:
        print("INVALID INPUT. Correct usage: python src/github_activity/main.py <username>")
        sys.exit(1)
    
    # Access the user through GitHub API 
    try:
        user_data = fetch_activity(username).json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"User '{username}' not found.")
        else:
            print(f"HTTP error: {e.response.status_code}")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        # No internet, DNS failure, refused connection
        print("Network error: could not reach the server")
        sys.exit(1)
    except requests.exceptions.Timeout:
        # Request took too long
        print("Request timed out")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # Catch-all for any requests error
        print(f"Something went wrong: {e}")
        sys.exit(1)
    else:
        if len(user_data) != 0:
            print("Output:")
            for event in user_data:
                print(format_event(event))
        else:
            print("No recent activity.")


if __name__ == "__main__":
    main()