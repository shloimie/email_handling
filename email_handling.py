import smtplib
import imaplib
import email

username = "autointernet910@gmail.com"
password = password
connection = ""
def start_send():
    global connection
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=username, password=password)
def send_main(send_to, message, subject="", ):
    global connection
    connection.sendmail(from_addr=username, to_addrs=send_to, msg="Subject:" + subject + "\n\n" + message)
def end_send():
    global connection
    connection.close()
def send_email(send_to, message, subject="", ):
    global  connection
    try:
        start_send()
        send_main(send_to, message , subject)
        end_send()
        print(f"email send to {send_to}")
    except:
        print(f"sending email did not work because of error ")


def get_inbox():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            # print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                # email_data['html_body'] = html_body.decode()
        my_message.append(email_data)

    return my_message
