import sys
import subprocess # creates a new process and runs the command in that process, also used for taking the IO from the command
 
#Checking IP reachability
def ip_reach(ip_add_list):
 
    for ip in ip_add_list:
        ip = ip.rstrip("\n")
        
        ping_reply = subprocess.call((f'ping {ip} /n 2'), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        # subprocess.call() used for executing shell command, waits for command to complete and returns sucess 0 or error code 
        # stdout and stderr ared used for output of the command and error of the command, we are using DEVNULL to suppress the output
        # this ping_reply will have 0 if the ping is successful and 1 if the ping is not successful
        
        if ping_reply == 0: # if ping_reply is 0 then the ip is reachable
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()


## test report:- 
# ip_add_list = ["192.168.0.1\n"]
# ip_reach(ip_add_list) # this will check if the ip is reachable or not, 