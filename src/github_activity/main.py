import sys 
from utils import validate_input

def main():
    # Get and validate user input 
    user_input = sys.argv[1:]
    if validate_input:
        username = user_input[0]
    else:
        print("Invalid input. Please enter a username.")

if __name__ == "__main__":
    main()