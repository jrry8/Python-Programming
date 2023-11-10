from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

# demo finding elements on the page
elem = browser.find_element(By.CLASS_NAME, "card-img-top")
print('Found <%s> element with that class name!' %(elem.tag_name))

# demo clicking the page
elem = browser.find_element(By.LINK_TEXT, "Subreddit")
elem.click()

# demo filling out and submitting forms
# find the <textarea> element for that text field 
browser.get('http://bing.com')
emailElem = browser.find_element(By.ID, "sb_form_q")
emailElem.send_keys("hello")
emailElem.submit()

