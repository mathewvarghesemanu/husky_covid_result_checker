website_url="https://securelink.labmed.uw.edu/seattleflu/"
husky_test_id="126ca1ae"
date_of_birth="06/13/1997"

#ignore everything beyond this point


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium	
import warnings
import easygui


warnings.filterwarnings("ignore")
chromedriver = 'C:\\Chromedriver\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get(website_url)

username = browser.find_element_by_id("barcode")
password = browser.find_element_by_id("dob")

username.send_keys(husky_test_id)
password.send_keys(date_of_birth)

browser.find_element_by_xpath("//*[@id=\"submitform\"]/div[3]/button").click()

status = browser.find_element_by_id("result-card")
if "pending" in status.text:
    easygui.msgbox("Result Pending", title="Covid test results")
else:
    easygui.msgbox("Result Arrived", title="Covid test results")
        
# print(status.text)

browser.quit()