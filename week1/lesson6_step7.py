from selenium import webdriver
from time import sleep
import math

link = "http://suninjuly.github.io/find_xpath_form"

def func(): 
    value1 = "input"
    value2 = "last_name"
    value3 = "city"
    value4 = "country"
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    func()
finally:
    time = sleep(30)
    browser.quit()


