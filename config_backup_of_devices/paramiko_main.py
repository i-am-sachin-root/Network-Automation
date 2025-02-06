"""
- used for implementing ssh protocol
- any device which can be configured by ssh can be configed by paramiko.
- repetative tasks can be automated. 
- pip install paramiko, to install paramiko library 
"""
import paramiko #importing paramiko library 
import time
import re 

host_ip = '192.168.81.180'
#creating ssh object
ssh_client = paramiko.SSHClient()  # creating ssh object. 

#print(ssh_client)

session = paramiko.SSHClient() #creating ssh object for client side ssh connection 
session.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #used for adding host key of remote device to the host keys of the local device
session.connect(hostname=host_ip, username='root', password='root',timeout=30,port=22,look_for_keys=False) #taking ip add from the list using username and password that we split and creating ssh connection  to remote host

print(f"connecting to {host_ip}")
#Start an interactive shell session on the remote device
connection = session.invoke_shell() #created shell object, invoking shell on the remote device, device will wait for the commands to be executed



# sending commands to the remote device (one by one), this is to go into config mode before taking commands from the file
connection.send("enable\n") # sending enable command, \n is to press enter
connection.send("terminal length 0\n") # this command disables the outout paging, all the config of command will be showed in one go
time.sleep(2) #waite for previous command to execute
connection.send("\n") # represent enter key
connection.send("configure terminal\n") #going into config mode
time.sleep(2)


# get the hostname of the device 
connection.send("do show running-config | include hostname\n")
time.sleep(2)
hostname_output = connection.recv(65535).decode("utf-8")

#getting hostname and filtering "hostname xyz" after running above command. 
match = re.search(r"hostname\s+(\S+)", hostname_output)
if match:
    device_hostname = match.group(1)
else:
    device_hostname = "Unknown_Device"


#getting the configuration from the device 
connection.send("do sh run\n")
time.sleep(2)
router_output = connection.recv(65535).decode("utf-8")



#putting the output into file which is hostname and ip specific. 
config_file = filename = f"{device_hostname}_{host_ip}.txt"
with open(filename, "w") as file:
    file.write(router_output)  #this will create the file in PWD

print(f"Configuration saved to {filename}")




# checking if the connection is open or close 
connection.close()
print("Connection closed")
