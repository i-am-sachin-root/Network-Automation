import threading #importted threading module
 
#Creating threads
def create_threads(ip_add_list, function): #taking the ip address list from ip_file_valid and function to run the ssh_connection file
 
    threads = [] #creating list to store thread objects
 
    for ip in ip_add_list: #looping throgh ip address list 
        th = threading.Thread(target = function, args = (ip,))   #creating thread object, target is ssh_connection function and for available ip int the list 
        th.start() #starting the thread
        threads.append(th) #appending all created ip address threads to the list
        
    for th in threads: #using the threads list to join all the threads and wait for them to finish
        th.join()