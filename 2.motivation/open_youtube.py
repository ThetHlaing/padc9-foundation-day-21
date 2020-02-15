## Open youtube page
## Get keyword randomly and search with it

## pip install selenium
## https://www.seleniumhq.org/
## https://selenium-python.readthedocs.io/
## https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

##open youtube page
browser = webdriver.Chrome('./drivers/chromedriver')
browser.get("https://www.youtube.com")


keywords = ["Motivation","Why should I study","Learning Motivation"]

random_keyword = keywords[random.randrange(len(keywords))]
##input search keyword and submit
search_input_box = browser.find_element_by_name("search_query")
search_input_box.clear()
search_input_box.send_keys("Python")
search_input_box.send_keys(Keys.RETURN)


##upgrade by randomly selecting the keyword