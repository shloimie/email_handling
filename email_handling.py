import smtplib
def send_email(send_to , subject , message):
    email_address = "autointernet910@gmail.com"
    password = "12345qwertY"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email_address , password= password)
    connection.sendmail(from_addr= email_address , to_addrs= send_to , msg= "Subject:"+ subject + "\n\n" + message)
    connection.close()

# send_email("hshloimie@gmail.com" , "this is function test" , "hello this is the body")

import imaplib
import pprint

imap_host = 'imap.gmail.com'
imap_user = "autointernet910@gmail.com"
imap_pass = "12345qwertY"

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)
imap.select('Inbox')
tmp, data = imap.search(None, 'ALL')
t, data = M.fetch('1', '(RFC822)')
body = data[0][1]
imap.close()

# trying pip install imapclient