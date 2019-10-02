from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time

# Данный метод заполняет поля 
def fillForm(browser): 
    value1 = "[name='firstname']"
    value2 = "[name='lastname']"
    value3 = "[name='email']"
    value4 = "file"
    value5 = ".btn"
    key1 = "Armin"
    key2 = "Van-Buren"
    key3 = "discoguy777@disco.org"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input1 = browser.find_element_by_css_selector(value1)
    input1.send_keys(key1)
    input2 = browser.find_element_by_css_selector(value2)
    input2.send_keys(key2)
    input3 = browser.find_element_by_css_selector(value3)
    input3.send_keys(key3)
    file_input = browser.find_element_by_id(value4)
    file_input.send_keys(file_path)
    browser.find_element_by_css_selector(value5).click()
    button.click()

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fillForm(browser)

    finally:
        time.sleep(5)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "https://SunInJuly.github.io/file_input.html"
test(link)

