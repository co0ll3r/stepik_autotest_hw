from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

def fillForm (browser):
    button = browser.find_element_by_id("button")
#    button.click()

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        fillForm(browser)

    finally:
        time.sleep(5)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "http://suninjuly.github.io/cats.html"
test(link)
