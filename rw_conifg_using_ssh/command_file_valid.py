import os.path
import sys

def command_file_valid():
     #take path of the file from user
        cred_file =  input("\n Enter path and filename of the file which contains commands: ")
        if os.path.isfile(cred_file) == True:
                print("file is valid")
        else:
                print("file is not valid")
                sys.exit() #exit the program if file is not valid

    