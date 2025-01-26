

# testing issues in ping function
# 
import time
import subprocess


def is_wan_link_up(WAN_IP):
    """Ping the WAN IP to check if it's reachable and display both stdout and stderr."""
    try:
        # Run the ping command and capture the output and error
        process = subprocess.Popen(
            f'ping {WAN_IP} -n 1', 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            shell=True
        )

        # Read the output and error from the process
        stdout, stderr = process.communicate()

        # Decode the byte output to strings for readability
        stdout = stdout.decode('utf-8')
        stderr = stderr.decode('utf-8')

        # Print or log stdout and stderr separately
        # print("Standard Output (stdout):")
        # print(stdout)  # Display the output of the ping command

        # print("Standard Error (stderr):")
        # print(stderr)  # Display any error messages

        # If the return code is 0 and no error phrase is found in stdout
        if process.returncode == 0 and "Destination host unreachable" not in stdout:
            # print(f"{WAN_IP} is reachable.")
            return 0  # Link is up, return 0
        else:
            # Check if the error message is in stdout (because Windows ping puts errors in stdout)
            if "Destination host unreachable" in stdout or "Request Timed Out" in stdout:
                # print(f"{WAN_IP} is unreachable. Error detected in output.")
                return 1
            else:
                # print(f"An unexpected error occurred. Error details: {stderr}")
                return 1  # Link is down or error occurred, return 1

    except Exception as e:
        # Handle any other errors in the ping process
        # print(f"Error while trying to ping {WAN_IP}: {e}")
        return 1  # Return 1 if any error occurs

# Test the function
WAN_IP = "192.168.0.147"
#is_wan_link_up(WAN_IP)




        




RETRY_COUNT = 4
#WAN_IP = "192.168.0.147"  # Example WAN IP
failed_attempts = 0
# Retry mechanism



while True:
    for i in range(RETRY_COUNT):
        if is_wan_link_up(WAN_IP) == 0:
            print(f"{WAN_IP} is reachable.")
            failed_attempts = 0
            break  # Break out of the for loop if the WAN IP is reachable
        else:
            failed_attempts += 1
            print(f"{WAN_IP} is unreachable. Attempt {i + 1}/{RETRY_COUNT}")
            time.sleep(10)  # Wait for 10 seconds before retrying
    
    time.sleep(5)