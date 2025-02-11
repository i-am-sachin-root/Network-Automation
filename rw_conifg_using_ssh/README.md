# Explanation of how this code works:

# File ip_file_validity.py-----------------------

1. **Checking File Validity:**
- The program prompts the user to enter the path and filename of the IP address file using the `input()` function.
- The function `os.path.isfile(ip_add_file)` is used to check if the file exists at the provided location.
- If the file exists, it prints "file is valid". If not, it prints "file is not valid" and exits the program using `sys.exit()`.
 - The program prompts the user to enter the path and filename of the IP address file using the `input()` function.
- The function `os.path.isfile(ip_add_file)` is used to check if the file exists at the provided location.
 - If the file exists, it prints "file is valid". If not, it prints "file is not valid" and exits the program using `sys.exit()`.

2. **Reading IP Addresses:**
 - Once the file is validated, the file is opened in read mode using `with open(ip_add_file, 'r')`.
- `f.seek(0)` moves the cursor to the beginning of the file.
- `f.readlines()` reads the content of the file line by line and stores it in the list `ip_add_list`. Each line corresponds to an IP address.

3. **Returning IP Addresses:**
- The list `ip_add_list`, which now contains all the IP addresses read from the file, is returned by the function.

4. **Test Example:**
 - You can test this function by calling it and printing the returned list, like so:
    Example usage:
        ip_list = ip_file_valid()
        print(ip_list)


# ip_add_validity.py-----------------------
### How It Works:

1. **Function Definition:**
   - The function `ip_addr_valid(ip_add_list)` accepts a list of IP addresses as input. The list contains IPs in string format, like `["192.168.0.1\n"]`.

2. **Removing Newline Character:**
   - Inside the loop, `ip.rstrip("\n")` is used to remove any newline character (`\n`) that is added by the `f.readlines()` method when reading the file.

3. **Splitting IP Address into Octets:**
   - Each IP address is split by periods (`.`) using `ip.split('.')`, which results in a list of octets (e.g., `['192', '168', '0', '1']`).

4. **Octet Validity Check:**
   - The function performs several checks on the IP address:
     - The address must have 4 octets (`len(octet_list) == 4`).
     - The first octet must be in the range 1-223, excluding multicast addresses and loopback addresses.
     - The address must not be part of the `169.254.x.x` range (APIPA).
     - All octets must be in the range 0-255.

5. **Invalid IP Handling:**
   - If an IP address does not pass the checks, the program prints an error message and stops using `sys.exit()`.

6. **Valid IP Handling:**
   - If the IP address is valid, the program continues to the next address without printing anything.



7. How to Use and Set Up:

- Save this module as `ip_add_validity.py` (or any name you prefer).
- Import the `ip_file_valid` function from `ip_file_validity.py` to get the list of IP addresses.
- Call the function `ip_addr_valid(ip_add_list)` with the list of IP addresses you want to validate.
- If all IPs are valid, the program continues without printing anything.
- If an invalid IP is found, the program exits and displays an error message with the invalid IP.



# cred_file_valid.py-----------------------
### **Summary: Checking File Availability for Login Credentials**

The `cred_file_valid` function is responsible for verifying the availability of a file containing login credentials (username and password) for devices. It ensures that the specified file exists at the given location before proceeding.

#### **How It Works:**
1. The user is prompted to input the path and filename of the credentials file.
2. The function uses `os.path.isfile()` to check if the specified file exists:
   - If the file exists:
     - A message confirms the file's validity.
   - If the file does not exist:
     - A message indicates the file is invalid.
     - The program exits using `sys.exit()` to prevent further execution.

#### **Purpose:**
This function is critical for validating that the credentials file is present and accessible. Without this check, subsequent operations requiring the file's content could fail.

#### **Example Usage:**
```python
cred_file_valid()
```
When called, the function prompts the user to input the path of the credentials file and validates its existence. This ensures that the necessary login credentials are available for authentication.

# ip_reachablity.py-----------------------
### **Summary: Checking IP Reachability**

The `ip_reach` function is designed to verify the reachability of a list of IP addresses by using the `ping` command. This function ensures that all specified devices are reachable on the network before proceeding with further operations.

#### **How It Works:**
1. The function takes a list of IP addresses (`ip_add_list`) as input.
2. For each IP address:
   - It removes any trailing newline characters using `rstrip("\n")`.
   - Executes the `ping` command with the IP address using `subprocess.call()`.
     - Sends 2 ICMP packets (`/n 2`) to the target IP.
     - Suppresses the command output and errors by redirecting `stdout` and `stderr` to `subprocess.DEVNULL`.
3. Based on the `ping` response:
   - If `ping_reply == 0`, the IP is reachable, and a success message is displayed.
   - If `ping_reply != 0`, the IP is unreachable, and the program terminates with an error message using `sys.exit()`.

#### **Purpose:**
This function ensures that all devices in the given list are accessible on the network, which is critical for any subsequent operations that rely on communication with these devices.

#### **Example Usage:**
```python
ip_add_list = ["192.168.0.1\n", "10.0.0.1\n"]
ip_reach(ip_add_list)
```
- This example checks the reachability of the specified IPs.
- If all IPs are reachable, the program proceeds.
- If any IP is unreachable, an error message is displayed, and the program exits.

#### **Key Notes:**
- **`subprocess.call()`:** Executes the `ping` command and waits for it to complete.
- **Return Codes:**
  - `0`: Ping successful.
  - Non-zero: Ping failed.
- **Output Suppression:** `subprocess.DEVNULL` prevents console clutter by suppressing command output and errors.

# command_file_valid.py-----------------------
### **Summary: Checking File Availability for Commands**

The `command_file_valid` function is used to verify the availability of a file that contains commands to be executed on devices. It ensures that the specified file exists at the provided location before proceeding.

#### **How It Works:**
1. The user is prompted to input the path and filename of the commands file.
2. The function uses `os.path.isfile()` to check if the specified file exists:
   - If the file exists:
     - A message confirms that the file is valid.
   - If the file does not exist:
     - A message indicates the file is invalid.
     - The program terminates using `sys.exit()` to prevent further execution.

#### **Purpose:**
This function ensures the availability of a valid commands file, which is necessary for executing tasks on devices. It prevents errors that could occur due to missing or incorrect file paths.

#### **Example Usage:**
```python
command_file_valid()
```
- When invoked, the function prompts the user to input the path of the commands file.
- It validates the file's existence to ensure subsequent operations can access the required commands.

#### **Key Notes:**
- **Validation:** The function is critical for avoiding runtime errors by ensuring the presence of a valid file before proceeding.
- **Error Handling:** If the file is not found, the program exits gracefully with an appropriate error message, prompting the user to correct the issue.




# command_file_valid.py-----------------------

### This Python script validates the path of a command file provided by the user.

# Function

- command_file_valid prompts the user for the path of a command file.
- It checks if the file exists using os.path.isfile().
- If the file is valid, it prints a message indicating so and returns the file path.
- If the file is invalid, it prints an error message and exits the program.

- Note

      The script allows the user to quit by entering 'q' at the prompt.



# handle_multiple_devices_thread.py-----------------------

This Python script uses the `threading` module to efficiently handle multiple SSH connections concurrently. The script takes a list of IP addresses and spawns a separate thread for each IP to execute SSH commands on remote devices.

### Key Components:

1. **`create_threads(ip_add_list, function)`**:
   - This function takes two arguments: `ip_add_list` (a list of IP addresses) and `function` (the function to execute on each IP).
   - It loops through the list of IP addresses, creating a thread for each one to run the specified function (typically `ssh_connection`).
   - Each thread is started immediately and added to a list for tracking.
   - After starting all threads, the function waits for each thread to complete by calling `join()` on each thread.

2. **Thread Management**:
   - The script ensures that all SSH connections are handled concurrently, significantly speeding up the process when dealing with multiple devices.
   - The threads are managed by appending them to a list and joining them at the end to ensure that all operations complete before moving on.

### Usage:

- This script is part of a larger network automation project where multiple remote devices are accessed simultaneously.
- It is typically used to execute SSH commands on multiple devices concurrently by creating threads for each device.



Here’s a summary for your `README.md` file for the `main.py` script:

---

# main.py-----------------------

This Python script automates SSH configurations on multiple devices by validating IP addresses, checking their reachability, and executing commands via SSH. It integrates several helper functions to ensure smooth execution and handles multiple devices concurrently using threading.

### Key Features:
1. **IP Address Validation**:
   - The script verifies the validity of each IP address in the provided file using `ip_file_validity` and `ip_add_validity` modules.
   - It ensures that only valid and non-conflicting IP addresses are processed.

2. **IP Reachability Check**:
   - It checks whether each IP address in the list is reachable via ICMP (ping).
   - If any device is not reachable, the script will exit with a message.

3. **Concurrent SSH Connections**:
   - The script creates threads for each device to allow concurrent SSH connections. This helps in executing commands on multiple devices simultaneously, improving performance.
   - It uses the `handle_multiple_devices_thread` module to manage these threads.

4. **SSH Commands Execution**:
   - After the connectivity and validation checks, the script triggers the `ssh_connection` function to establish SSH sessions and execute predefined commands on each reachable device.
   
### How It Works:
1. **Input Files**:
   - The script reads a file containing a list of IP addresses (`ip.txt`), a file with device credentials (`credentials.txt`), and a file with commands to be executed (`commands.txt`).

2. **Execution Flow**:
   - The IP addresses from the input file are validated and checked for reachability.
   - Threads are created for each reachable IP to perform SSH connections and execute commands concurrently.


### Dependencies:
- `sys`
- `subprocess`
- `threading`
- Custom modules: `ip_file_validity`, `ip_add_validity`, `ip_reachablity`, `ssh_connection`, `handle_multiple_devices_thread`

### Notes:
- The script expects specific formats for the IP addresses, credentials, and commands in the input files.
- If an IP address is unreachable, the script will terminate early.
- The script can be extended or modified for other automation tasks as needed.



# How to use-----------------------
   1. run main.py
   1. then add paths simultaneously  
       D:\Codes\Network-Automation\rw_conifg_using_ssh\credentials.txt --> inside file root,root (you have to configure ssh ver 2 and use same password for enable and login. )
       D:\Codes\Network-Automation\rw_conifg_using_ssh\commands.txt    --> the commnds you want to put
       D:\Codes\Network-Automation\rw_conifg_using_ssh\ip_add_file.txt  --> ip addresses of your remote machine
   2. check files have entered requred details like pass and username, ip,commands etc. 
   3. your commands will sent to device via ssh and output will be shown at python prompt. 



