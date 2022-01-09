from imapclient import IMAPClient

imap_user = "autointernet910@gmail.com"
imap_pass = "12345qwertY"

imap_host = 'imap.gmail.com'
server = IMAPClient('imap.gmail.com', use_uid=True)
server.login(imap_user, imap_pass)

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])

messages = server.search(['FROM', 'hshloimie@gmail.com'])
print("%d messages from our best friend" % len(messages))


for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

server.logout()