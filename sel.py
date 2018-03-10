import time
from selenium import webdriver


def search(text):
    driver = webdriver.Chrome('G:\minor project\chromedriver.exe')
    driver.get('http://www.google.com')
    time.sleep(2)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(text)
    search_box.submit()
    time.sleep(5)
#search("mayank mahavar")