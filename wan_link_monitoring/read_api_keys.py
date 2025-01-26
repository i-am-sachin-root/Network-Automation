import sys
import os

def read_api_keys():
    """Read the API keys from a file."""

    # note:- DO not add your credentials directly in any file and repo, keep it safe.  
    api_file = "D:\\API cred do not shared\\apicred.txt"

    # Check for quit option
    # if api_file.lower() == 'q': 
    #     sys.exit()
    
    # # Validate file existence
    # if os.path.isfile(api_file):
    #     print("File is valid.")
    # else:
    #     print("File is not valid. Please provide a valid file path.")
    #     sys.exit()

    # Read and process the file
    try:
        with open(api_file) as file:
            keys = file.read().splitlines()  # Read all lines and split into a list

            # Ensure the file has at least 4 lines
            if len(keys) < 4:
                print("Error: The file must contain at least 4 lines (API key, API secret, from email, to email).")
                sys.exit()

            # Extract required values
            api_keys = keys[0].rstrip("\n")
            api_secret = keys[1].rstrip("\n")
            from_email = keys[2].rstrip("\n")
            to_email = keys[3].rstrip("\n")
        
        return api_keys, api_secret, from_email, to_email

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit()

# Example usage of the function
if __name__ == "__main__":
    try:
        api_key, api_secret, from_email, to_email = read_api_keys()
        # Now you can use these values in your program
        print("API Key:", api_key)
        print("API Secret:", api_secret)
        print("From Email:", from_email)
        print("To Email:", to_email)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
