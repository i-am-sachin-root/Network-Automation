import os.path
import sys
 
#Checking IP address file and content validity
def ip_file_valid():

        #take path of the file from user
        ip_add_file =  input("\n Enter path and filename of the file which contains IP addresses: ")
        if os.path.isfile(ip_add_file) == True:
                print("file is valid")
        else:
                print("file is not valid")
                sys.exit() #exit the program if file is not valid

        # open ip_add_file and read the addresses
        with open(ip_add_file, 'r') as f: #creating a file object and opening the file in read mode
               f.seek(0) # moved cursor to the start of the file
               ip_add_list = f.readlines() #reading the file line by line and storing in a list
               f.close()
               return ip_add_list

# test :- file working as intetended 
ip_file_valid()