

imap_user = "autointernet910@gmail.com"
imap_pass = "12345qwertY"

imap_host = 'imap.gmail.com'
import email
from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = "autointernet910@gmail.com"
PASSWORD = "12345qwertY"

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    server.select_folder("INBOX", readonly=True)

    messages = server.search("UNSEEN")
    for uid, message_data in server.fetch(messages, "RFC822").items():
        email_message = email.message_from_bytes(message_data[b"RFC822"])
        print(uid, email_message.get("From"), email_message.get("Subject"))
        print(email_message.get())