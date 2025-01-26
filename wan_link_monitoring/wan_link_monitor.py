import os
import sys
import time
import subprocess
from mail_alert import send_email  # Import the email function from email_alert.py
from ip_file_validity import ip_file_valid # Import the function to check the validity of the IP address file
from ip_add_validity import ip_addr_valid # Import the function to check the validity of the IP addresses


# taking the list of ip from file
ip_list = ip_file_valid() 

# checking the ip is valid or not
ip_addr_valid(ip_list)

#taking the 1st ip, we can do for multiple ip's from list but we need to create multithreading.
WAN_IP = ip_list[0].strip()


#print(type(WAN_IP))
# PING_INTERVAL = 5   # Time in seconds between each ping
RETRY_COUNT = 4      # Number of retries before declaring WAN as down

#ip_addr_valid(WAN_IP) # Check the validity of the WAN IP address

# def is_wan_link_up(WAN_IP): #this function will check if ip is reachable or not, we'll us only 1 ping 
#     """Ping the WAN IP to check if it's reachable."""
#     ping_reply = subprocess.call((f'ping {WAN_IP} -n 1'), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL,shell=True) # using subpreocess to interact with the system shell
#     return ping_reply # if ping is successful then return 0, if not then return 1q

# debugging ping function
# def is_wan_link_up(WAN_IP):
#     """Ping the WAN IP to check if it's reachable."""
#     ping_reply = subprocess.call(f'ping {WAN_IP} -n 2', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
#     print(f"ping_reply for {WAN_IP}: {ping_reply}")  # Debugging print to check the ping reply value
#     return ping_reply  # If ping is successful, it should return 0, otherwise a non-zero value


# # deep debugging for ping 
# def is_wan_link_up(WAN_IP):
#     """Ping the WAN IP to check if it's reachable."""
#     result = subprocess.run(f'ping {WAN_IP} -n 1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     print(f"ping_reply for {WAN_IP}: {result.returncode}")  # Debugging print to check the return code
#     print(f"Ping output: {result.stdout.decode()}")  # Print the actual ping response
#     print(f"Error output: {result.stderr.decode()}")  # Print any error messages
#     return result.returncode  # Returns 0 if successful, non-zero if failed

# modified ping function 
def is_wan_link_up(WAN_IP):
    """Ping the WAN IP to check if it's reachable and no errors occur."""
    try:
        # Run the ping command and capture the output and error
        ping_reply = subprocess.call(f'ping {WAN_IP} -n 1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
        # Capture any error output
        error_output = subprocess.PIPE

        # Check if the return code is 0 (indicating success) and there's no error
        if ping_reply == 0 and error_output is None:
            return 0  # Link is up, return 0
        else:
            return 1  # Link is down or error occurred, return 1

    except Exception as e:
        # Handle any other errors in the ping process
        print(f"Error while trying to ping {WAN_IP}: {e}")
        return 1  # Return 1 if any error occurs



def monitor_wan(): # creating function to monitor the WAN link
    """Monitor the WAN link and send an email if it goes down."""
    print(f"Monitoring WAN link: {WAN_IP}")
    link_status = None #storing status outside of while loop so the stored value does not reset on each while loop
    while True:
        
        failed_attempts = 0

        # Retry mechanism
        for i in range(RETRY_COUNT): # loop till retry count
            if is_wan_link_up(WAN_IP) == 0: # if wan ip is reachable
                print(f"{WAN_IP} is reachable.") # then print reachable
                failed_attempts = 0 # reset failes attempts to 0
                break # if reachable then break the for loop
            else: # if not reachable
                failed_attempts += 1 # this will increment the fasiled attempts till for loop ends
                print(f"{WAN_IP} is unreachable. Attempt {i + 1}/{RETRY_COUNT}") # 1/4 tries, i+1 because i starts from 0
                time.sleep(10)

        # Send email if WAN is down
        if failed_attempts == RETRY_COUNT:
            if link_status != "down":  # If the link was not already marked as down
                print(f"WAN link {WAN_IP} is down. Sending email notification.")
                send_email(subject="WAN Link Down Alert", message=f"The WAN link to {WAN_IP} is down. Please check the connectivity.")  # Send "link down" email
                link_status = "down"  # Update the status to "down"

        # If WAN is up
        if failed_attempts < RETRY_COUNT:
            if link_status != "up":  # If the link was not already marked as up
                print(f"WAN link {WAN_IP} is back up. Sending email notification.")
                send_email(subject="WAN Link Up Alert", message=f"The WAN link to {WAN_IP} is back up and running.")  # Send "link up" email
                link_status = "up"  # Update the status to "up"
        
        time.sleep(5) # run while loop every 10 seconds
        
        #break # break the loop after 1 iteration
        # print("Email sent. Stopping the monitoring.")
        # break  # Exit the loop after sending the email

# checking if this file is main file or imported
if __name__ == "__main__": # if run directly then name set to main, if impoted then name is set to file name wan_link_monitor, checking file is main or imported
    try:
        print("starting WAN link monitoring...use ctl + c to stop")
        monitor_wan() # calling monitor_wan function
    except KeyboardInterrupt: # if user press ctrl+c then this block will execute
        print("Monitoring stopped.")


