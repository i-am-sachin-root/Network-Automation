# creating file which will file availablity for login credentails in devices 
import os.path
import sys

def cred_file_valid():
     #take path of the file from user
        cred_file =  input("\n Enter path and filename of the file which contains username and pass: ")
        if os.path.isfile(cred_file) == True:
                print("file is valid")
                return cred_file
        else:
                print("file is not valid")
                sys.exit() #exit the program if file is not valid

    

#cred_file_valid() # calling function to test it