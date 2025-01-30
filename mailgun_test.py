import requests

MAILGUN_API_KEY = 'be616489f3c44adc72dd4c110dab9e40-d8df908e-bd4e8b87'
MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandbox5e486bc37b9743d29741b431b148edba.mailgun.org/messages'
FROM_EMAIL_ADDRESS = 'mailgun@sandbox5e486bc37b9743d29741b431b148edba.mailgun.org'

def send_email(to_address: str, subject: str, message: str):
    resp = requests.post(
        MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,
            "text": message
        }
    )

    if resp.status_code == 200:
        print("Email sent successfully")
    else:
        print(f"Failed to send email. Status code: {resp.status_code}")
        print(resp.text)
    
send_email("daria.alekseeva@slice.com", "Test Subject", "This is a test message")


