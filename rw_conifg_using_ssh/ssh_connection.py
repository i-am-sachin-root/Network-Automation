import paramiko # used for ssh connection
import os.path # used to interact with the file system
import time # used for sleep function and other time related functions
import sys # used for system specific parameters and functions
import re # used for regular expression matching

from cred_file_validity import cred_file_valid #importing function from cred_file_validity.py
from command_file_valid import command_file_valid #importing function from command_file_validity.py

#Checking username/password file
#Prompting user for input - USERNAME/PASSWORD FILE
cred_file = cred_file_valid()
        
#Checking commands file
#Prompting user for input - COMMANDS FILE
cmd_file = command_file_valid()



#Open SSHv2 connection to the device
def ssh_connection(ip):
    
    global cred_file
    global cmd_file
    
    try:
        #opening file in read mode and reading the username and password
        with open(cred_file, 'r') as selected_cred_file: #opening file in read mode and creating a file object
            selected_cred_file.seek(0) # moved cursor at the start of file
            username = selected_cred_file.readlines()[0].split(',')[0] #reading 1st line from file and then taking the 1st username from it by splitting username and password by ','
            selected_cred_file.seek(0)  #going back to the start of the file
            password = selected_cred_file.readlines()[0].split(',')[1].rstrip("\n") #taking password now and removing \n from the end of the password


            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.connect(ip.rstrip("\n"), username=username, password=password)
            
            connection = session.invoke_shell()
            connection.send("enable\n")
            connection.send("terminal length 0\n")
            time.sleep(1)
            connection.send("\n")
            connection.send("configure terminal\n")
            time.sleep(1)
            selected_cmd_file = open(cmd_file, 'r')
            selected_cmd_file.seek(0)
            for each_line in selected_cmd_file.readlines():
                connection.send(each_line + '\n')
                time.sleep(2)
            selected_cred_file.close()
            selected_cmd_file.close()
            router_output = connection.recv(65535)
            if re.search(b"% Invalid input", router_output):
                print("* There was at least one IOS syntax error on device {} :(".format(ip))
            else:
                print("\nDONE for device {} :)\n".format(ip))
            print(str(router_output) + "\n")
            session.close()
    except paramiko.AuthenticationException:
            print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
            print("* Closing program... Bye!")
