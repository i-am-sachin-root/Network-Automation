

# testing issues in ping function
# 
import time
import subprocess
def is_wan_link_up(WAN_IP): #this function will check if ip is reachable or not, we'll us only 1 ping 
    """Ping the WAN IP to check if it's reachable."""
    ping_reply = subprocess.call((f'ping {WAN_IP} -n 2'), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL,shell=True) # using subpreocess to interact with the system shell
    # if  ping_reply == 0: # if ping is successful then return 0, if not then return 1q
    #     print("success")
    # else:
    #     print("failed")
    return ping_reply
        

#is_wan_link_up('192.168.0.147')



RETRY_COUNT = 4
WAN_IP = "8.8.8.8"  # Example WAN IP
failed_attempts = 0
# Retry mechanism
for i in range(RETRY_COUNT):
    if is_wan_link_up(WAN_IP) == 0:
        print(f"{WAN_IP} is reachable.")
        failed_attempts = 0
        break
    else:
        failed_attempts += 1
        print(f"{WAN_IP} is unreachable. Attempt {i + 1}/{RETRY_COUNT}")
        time.sleep(10)