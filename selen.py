from web_handler import WebHandleing as wh
import time
def prog(website):
	new = wh()
	website = new.check_url(website)
	new.get(website)
	new.send_tabs(1)
	new.screen()
	time.sleep(50)

prog("myzmanim")
# prog("http://www.google.com")
