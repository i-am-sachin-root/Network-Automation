import os.path
import sys

def command_file_valid():
     #take path of the file from user
        cmd_file =  input("\n Enter path and filename of the file which contains commands. * press 'q' to quite: ")
        while cmd_file == 'q': 
                sys.exit()
        if os.path.isfile(cmd_file) == True:
                print("file is valid")
                return cmd_file 
        else:
                print("file is not valid")
                sys.exit() #exit the program if file is not valid

    