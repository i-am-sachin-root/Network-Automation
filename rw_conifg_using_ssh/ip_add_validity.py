import sys
#from ip_file_validity import ip_file_valid
#ip_add_list = ["192.168.0\n"] test address
#Checking octets
def ip_addr_valid(ip_add_list): #we will take list of ip addresses       
 
    for ip in ip_add_list: # go throgh ip add which will be like ["192.168.0.1\n"] list of strings
        ip = ip.rstrip("\n") # remove \n from end of ip add, this \n will be added by readlines() method
        octet_list = ip.split('.') #this will split ip add into list denominated by '.' so list will look like ['192', '168', '0', '1']
        

        #Checking octet validity
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        # 1st yellow bracket is to  check if the list contains 4 octets ['192', '168', '0', '1']
        # 2nd yellow bracket is to check if 1st octate is 1 < octate < 223, we are trying to exclude multicast and reserved addresses
        # 3rd yellow bracket is to check if 1st occtate is not from loopback addresses
        # 4th yellow bracket is to check if 2nd and 3rd octate are not 169 and 254, checking for APIPA and broadcast addresses
        # 5 6 7 yellow octate is to check if 2nd 3rd and 4th octate are in range 0-255
        else:
            print(f'\n* There was an invalid IP address in the file: {ip} :(\n')
            sys.exit()  # exit programm if ip address not valid 

#print(ip_addr_valid(ip_add_list)) calling fubnction to test it

# test report:- if ip is correct then nothing is printed, continue will go to next ip add in list, but if the ip does not match the ip condition then execute the else block and exit the program.