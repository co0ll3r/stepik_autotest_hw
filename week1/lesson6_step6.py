from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/huge_form.html"

def func(): 
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("ABRWALK")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    func()
finally:
    time = sleep(30)
    browser.quit()


