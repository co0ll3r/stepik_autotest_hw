from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

# Рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Данный метод заполняет поля 
def fillForm(browser): 
    value1 = "input_value"
    value2 = "answer"
    value3 = "robotCheckbox"
    value4 = "robotsRule"
    value5 = "[type='submit']"
    x = calc(browser.find_element_by_id(value1).text)
    input1 = browser.find_element_by_id(value2)
    input1.send_keys(x)
    browser.find_element_by_id(value3).click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id(value4).click()
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
link = "https://SunInJuly.github.io/execute_script.html"
test(link)
