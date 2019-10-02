from selenium import webdriver
import math
import time

# Рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Данный метод заполняет поля 
def fillForm(browser): 
    value1 = "treasure"
    value2 = "answer"
    value3 = "robotCheckbox"
    value4 = "robotsRule"
    value5 = "[type='submit']"
    x = calc(browser.find_element_by_id(value1).get_attribute("valuex"))
    print(x)
    input1 = browser.find_element_by_id(value2)
    input1.send_keys(x)
    browser.find_element_by_id(value3).click()
    browser.find_element_by_id(value4).click()
    browser.find_element_by_css_selector(value5).click()

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fillForm(browser)

    finally:
        time.sleep(10)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link1 = "http://suninjuly.github.io/get_attribute.html"
test(link1)

