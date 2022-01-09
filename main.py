import email_handling as eh

eh.start_send()
eh.send_main(send_to="autointernet910@gmail.com", message="this is a test of non-class module")
eh.send_main(send_to="autointernet910@gmail.com", message="this is email number 2 in a shot")
eh.end_send()

my_inbox = eh.get_inbox()
for thing in my_inbox:
    from_ = thing["from"]
    body = thing["body"].strip()
    print(from_ + body)




