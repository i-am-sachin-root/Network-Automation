import requests

# Mailjet API credentials
from read_api_keys import read_api_keys
MAILJET_API_KEY, MAILJET_API_SECRET, FROM_EMAIL, TO_EMAIL = read_api_keys()



def send_email(subject, message):
    """Send an email using the Mailjet API."""
    url = "https://api.mailjet.com/v3.1/send"
    headers = {
        "Content-Type": "application/json"
              }
    data = {
        "Messages": [
            {
                "From": {"Email": FROM_EMAIL},
                "To": [{"Email": TO_EMAIL}],
                "Subject": subject,
                "TextPart": message
            }
        ]
    }
    try:
        response = requests.post(url, auth=(MAILJET_API_KEY, MAILJET_API_SECRET), json=data)
        if response.status_code == 200:
            print("Email sent successfully.")
        else:
            print(f"Failed to send email. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
