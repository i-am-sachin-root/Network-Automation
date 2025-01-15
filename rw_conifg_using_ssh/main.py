#Importing the necessary modules
import sys
 
from ip_file_validity import ip_file_valid
from ip_add_validity import ip_addr_valid
from ip_reachablity import ip_reach
from ssh_connection import ssh_connection #this fubction is calling 2 functions which are cred_file = cred_file_valid() and cmd_file = command_file_valid()
from handle_multiple_devices_thread import create_threads
 
#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()
 
#Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
 
#Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
 
#Calling threads creation function for one or multiple SSH connections
create_threads(ip_list, ssh_connection)
 
#End of program