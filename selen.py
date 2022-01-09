from web_handler import WebHandleing as wh
import time
def prog(website):
	new = wh()
	website = new.check_url(website)
	new.get(website)
	new.send_tabs(1)
	time.sleep(50)

	# ip_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
	# ip_box.send_keys("some text",Keys.ENTER)

	# driver.save_screenshot('screenie.png')
	# time.sleep(60)

prog("myzmanim")
# prog("http://www.google.com")
