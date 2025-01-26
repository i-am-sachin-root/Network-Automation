# WAN Link Monitoring System

This repository contains a set of Python scripts that work together to monitor the status of a WAN link and send email notifications when the link goes down or comes back up. It also validates the IP address file and the IP addresses within it. The email notifications are sent using the Mailjet API.

## Files Overview

### 1. `wan_link_monitor.py`

#### Purpose:
This is the main script responsible for monitoring a WAN link. It continuously checks if the WAN IP is reachable and sends an email notification when the link goes down or comes back up.

#### Key Functions:
- **`is_wan_link_up(WAN_IP)`**:
  - Pings the provided WAN IP to check if it’s reachable.
  - Returns `0` if the IP is reachable, `1` if it’s unreachable.

- **`monitor_wan()`**:
  - Monitors the WAN link in a continuous loop.
  - Uses the `is_wan_link_up` function to check if the WAN link is up or down.
  - Attempts to ping the WAN IP a certain number of times (configured by `RETRY_COUNT`).
  - Sends an email when the WAN link goes down or comes back up, using the `send_email` function from the `mail_alert.py` file.

#### How It Works:
- The file reads the IP addresses from a file (via `ip_file_validity.py`).
- It checks whether the IP is reachable.
- If the link goes down (i.e., the IP is unreachable for the specified retries), it sends an email notification.
- When the link comes back up, it sends another email to notify that the WAN link is back up.

---

### 2. `read_api_keys.py`

#### Purpose:
This file handles the reading of API keys and email credentials from a text file to send email notifications using the Mailjet API.

#### Key Functions:
- **`read_api_keys()`**:
  - Reads the API keys and email addresses from a file (`apicred.txt`).
  - Ensures the file contains at least four lines (API key, API secret, from email, and to email).
  - Returns the extracted API keys and email addresses.

#### How It Works:
- The file opens `apicred.txt`, which should contain the Mailjet API credentials (API key, API secret) and the email addresses (from email and to email).
- The function ensures that the file contains valid data (at least four lines).
- It then returns these values so they can be used by other scripts (like in `mail_alert.py` to send emails).

---

### 3. `mail_alert.py`

#### Purpose:
This file is responsible for sending email notifications using the Mailjet API.

#### Key Functions:
- **`send_email(subject, message)`**:
  - Sends an email with the provided `subject` and `message`.
  - Uses the credentials and email addresses fetched from `read_api_keys.py`.
  - Sends the email to the specified recipient using Mailjet's API.

#### How It Works:
- The function is called in `wan_link_monitor.py` when the WAN link goes down or comes back up.
- It constructs an email message and sends it using the Mailjet API with the credentials provided.
- The email contains a subject and message indicating whether the WAN link is down or up.

---

### 4. `ip_file_validity.py`

#### Purpose:
This file checks if the IP address file is valid and reads the IP addresses from it.

#### Key Functions:
- **`ip_file_valid()`**:
  - Prompts the user for the path of the IP address file.
  - Validates if the file exists.
  - Reads the file and returns the list of IP addresses.

#### How It Works:
- The user is prompted to input the path of the file that contains the IP addresses to be monitored.
- It checks if the file exists using `os.path.isfile()`.
- The file content is read line by line and returned as a list of IP addresses to be used in `wan_link_monitor.py`.

---

### 5. `ip_add_validity.py`

#### Purpose:
This file checks the validity of the IP addresses provided in the list.

#### Key Functions:
- **`ip_addr_valid(ip_add_list)`**:
  - Validates the format of each IP address in the list.
  - Ensures each IP address has four octets, and checks that the octets are within valid ranges.
  - If any IP address is invalid, the program will exit and print an error message.

#### How It Works:
- The function checks if each IP address follows the standard format (`xxx.xxx.xxx.xxx`), where each octet is between 0 and 255.
- It excludes invalid IP addresses such as loopback addresses (`127.x.x.x`), APIPA addresses (`169.254.x.x`), and multicast addresses.
- If an invalid IP is found, the program prints an error and terminates.

---

### 6. `ip_add_file.txt`

#### Purpose:
This text file contains the IP addresses to be monitored by the WAN link monitoring script.

#### Content:
- The file should contain one IP address per line.
- Example content: 8.8.8.8

#### How It Works:
- This file is read by the `ip_file_validity.py` file.
- The list of IP addresses is passed to the `wan_link_monitor.py` file to be monitored for connectivity.
- If the file contains any invalid IP addresses, the program will exit and show an error.

---

## How to Use

1. **Prepare the Files**:
 - Make sure the `ip_add_file.txt` contains a list of valid IP addresses you want to monitor.
 - Add your Mailjet API credentials (API Key, API Secret) and email addresses (From, To) in the `apicred.txt` file.
 
2. **Run the Main Script**:
 - Run the `wan_link_monitor.py` script. It will:
   - Read the list of IP addresses from the file (`ip_add_file.txt`).
   - Validate each IP address.
   - Continuously monitor the WAN link status.
   - Send email notifications when the WAN link goes down or comes back up.

3. **Dependencies**:
 - Make sure you have the necessary dependencies installed, such as `requests` for sending emails via Mailjet:
   ```
   pip install requests
   ```

4. **Customizing**:
 - You can change the `RETRY_COUNT` and the sleep intervals in `wan_link_monitor.py` to suit your needs.
 - Modify the email message and subject in `mail_alert.py` as needed.

---
