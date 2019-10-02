from selenium import webdriver
from time import sleep
import math

link = "http://suninjuly.github.io/find_link_text"

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
    button = browser.find_element_by_class_name("btn-default")
    button.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    val1 = str(math.ceil(math.pow(math.pi, math.e)*10000))
    transition = browser.find_element_by_link_text(val1)
    transition.click()
    func()
finally:
    time = sleep(30)
    browser.quit()


