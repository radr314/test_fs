# import requests
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2 import service_account
import base64
# import email
from pathlib import Path


load_dotenv()

gmail_secrets_path=Path(r'C:\Users\ranad\Desktop\syncc\acloop\secrets\GmailOauthCredentials_rv131_gcp')
service_secrets_path = Path(r'C:\Users\ranad\Desktop\syncc\acloop\secrets\serviceaccount_utilityservice_gcp')

from google.oauth2.credentials import Credentials
# Load Gmail API Credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIALS_FILE = gmail_secrets_path / 'credentials.json'
SERVICE_ACCOUNT_CREDENTIALS= service_secrets_path / 'credentials.json'
from google_auth_oauthlib.flow import InstalledAppFlow
def get_gmail_service():
    """Authenticate and return the Gmail API service"""
    # creds = service_account.Credentials.from_service_account_file(
    #     CREDENTIALS_FILE, scopes=SCOPES
    # )
    # creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)

    # if not creds or not creds.valid:
    token_file = "token.json"
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(token_file, "w") as token:
        token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_messages(service, user_id='randheerv131@gmail.com', max_results=10):
    """Retrieve messages from Gmail"""
    result = service.users().messages().list(userId=user_id, maxResults=max_results).execute()
    return result.get('messages', [])

def get_email_content(service, msg_id, user_id='randheerv131@gmail.com'):
    """Retrieve and parse an email by ID"""
    msg = service.users().messages().get(userId=user_id, id=msg_id, format='full').execute()
    headers = msg['payload']['headers']

    # Extract subject and sender
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
    sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")

    # Decode email body
    body = "No Body"
    if 'parts' in msg['payload']:
        for part in msg['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                body_data = part['body']['data']
                body = base64.urlsafe_b64decode(body_data).decode('utf-8')

    return {"From": sender, "Subject": subject, "Body": body}

# Run the Gmail reader
if __name__ == "__main__":
    service = get_gmail_service()
    messages = get_messages(service, max_results=5)  # Get latest 5 emails

    for msg in messages:
        email_data = get_email_content(service, msg['id'])
        print(f"📩 **From:** {email_data['From']}")
        print(f"📌 **Subject:** {email_data['Subject']}")
        print(f"📜 **Body:**\n{email_data['Body']}")
        print("=" * 50)
