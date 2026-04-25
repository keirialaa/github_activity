import sys 
import requests 

from utils import validate_input, format_event

def main():

    def fetch_activity(username):
        response = requests.get(f"https://api.github.com/users/{username}/events")
        response.raise_for_status()
        return response

    # Get and validate user input 
    user_input = sys.argv[1:]
    if validate_input:
        username = user_input[0]
    else:
        print("Invalid input. Please enter a username.")
        sys.exit(1)
    
    # Access the user through GitHub API 
    try:
        user_data = fetch_activity(username).json()
    except requests.exceptions.HTTPError as e:
        # 404, 403, 500 etc.
        print(f"HTTP error: {e}")
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