from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

def fillForm (browser):
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        fillForm(browser)

    finally:
        time.sleep(7)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "http://suninjuly.github.io/wait2.html"
test(link)
