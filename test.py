import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import time
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, msg_text):
    message = MIMEText(msg_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def main():
    service = get_gmail_service()
    recipient = input("Enter recipient email: ")
    interval = float(input("Enter interval in seconds (minimum 5): "))
    interval = max(5, interval)

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = create_message(
                "me",
                recipient,
                "Test Email",
                f"Test message sent at {timestamp}"
            )
            
            service.users().messages().send(userId="me", body=message).execute()
            print(f"Email sent at {timestamp}")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nStopping email sender")

if __name__ == '__main__':
    main()