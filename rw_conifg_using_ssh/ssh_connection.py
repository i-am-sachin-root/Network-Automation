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
    #username = "root"
    #password = "root"
    
    try:
        #opening file in read mode and reading the username and password
        with open(cred_file, 'r') as selected_cred_file: #opening file in read mode and creating a file object
            selected_cred_file.seek(0) # moved cursor at the start of file
            username = selected_cred_file.readlines()[0].split(',')[0].rstrip("\n") #reading 1st line from file and then taking the 1st username from it by splitting username and password by ','
            selected_cred_file.seek(0)  #going back to the start of the file
            password = selected_cred_file.readlines()[0].split(',')[1].rstrip("\n") #taking password now and removing \n from the end of the password

            #Logging into device using paramiko 
            session = paramiko.SSHClient() #creating ssh object for client side ssh connection 
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #used for adding host key of remote device to the host keys of the local device
            session.connect(ip.rstrip("\n"), username=username, password=password,timeout=30,port=22,look_for_keys=False) #taking ip add from the list using username and password that we split and creating ssh connection  to remote host

            #Start an interactive shell session on the remote device
            connection = session.invoke_shell() #created shell object, invoking shell on the remote device, device will wait for the commands to be executed

            # sending commands to the remote device (one by one), this is to go into config mode before taking commands from the file
            connection.send("enable\n") # sending enable command, \n is to press enter
            connection.send("terminal length 0\n") # this command disables the outout paging, all the config of command will be showed in one go
            time.sleep(2) #waite for previous command to execute
            connection.send("\n") # represent enter key
            connection.send("configure terminal\n") #going into config mode
            time.sleep(2)

           
            with open(cmd_file, 'r') as selected_cmd_file: #oprning file and creating file object
                selected_cmd_file.seek(0) # moving cursor to the start of the file
                for f in selected_cmd_file.readlines(): #taking coommnd from readlines() method list of commands, and using for loop to enter every command.
                    connection.send(f + '\n') #using shell object to send command to the remote device
                    time.sleep(2)
               

            router_output = connection.recv(65535) # taking the last output of the command
            router_output = router_output.replace(b'\r\n', b'\n') # replacing \r\n with \n in the output
            if re.search(b"% Invalid input", router_output): # using regx to sesrch for error in the output
                print(f"* There was at least one IOS syntax error on device {ip} :(") # if error is found then print this
            else:
                print(f"\ncommands pushed to remote deivce {ip} :)\n") # if no error is found then print this
            print(router_output.decode('utf-8')) # print the output of the last command 
            session.close()
    # except paramiko.AuthenticationException:
    #         print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
    #         print("* Closing program... Bye!")

    except paramiko.SSHException as e:
        print(f"Paramiko SSH error: {e}")
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed: {e}")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
#checking if the file is being run directly or being imported
#ssh_connection("192.168.81.171")