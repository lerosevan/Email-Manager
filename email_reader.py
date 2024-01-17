from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def read_emails(creds):
    # Create the service object
    service = build('gmail', 'v1', credentials=creds)

    # Code to get messages
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        print("Sender names and email addresses:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            # Extract sender information from headers
            sender = next(header['value'] for header in msg['payload']['headers'] if header['name'] == 'From')
            print(sender)
