# WAN Link Monitoring System

This project is designed to monitor a WAN link by checking its connectivity and sending email notifications when the link goes down or comes back up. The system reads a list of IP addresses from a file, validates them, and uses the Mailjet API to send alerts.

## Files Overview

### 1. `wan_link_monitor.py`
- Main script that monitors the WAN link.
- Reads the IP addresses from the file, validates them, and pings the WAN IP to check if it's reachable.
- Sends email alerts when the WAN link is down or back up.
- Utilizes the `send_email` function from `mail_alert.py`.

### 2. `read_api_keys.py`
- Reads the Mailjet API credentials and email addresses from a file (`apicred.txt`).
- The file should contain the following keys in order: API key, API secret, from email, and to email.
- Validates the file's content before use.

### 3. `mail_alert.py`
- Contains the `send_email` function which sends email alerts via the Mailjet API.
- Uses the API key, API secret, from email, and to email, imported from `read_api_keys.py`.

### 4. `ip_file_validity.py`
- Reads the file containing the IP addresses to be monitored.
- Validates the file existence and ensures it contains valid IP addresses.

### 5. `ip_add_validity.py`
- Checks the validity of each IP address in the list.
- Ensures the IP addresses are in valid format and are not from reserved or multicast ranges.

### 6. `ip_add_file.txt`
- A text file containing the IP addresses to be monitored. Example: `8.8.8.8`.

## Requirements

- Python 3.x
- Requests library (for Mailjet API integration)

Install the required libraries by running:

```bash
pip install requests
