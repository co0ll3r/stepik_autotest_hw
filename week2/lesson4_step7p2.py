from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fillForm (browser):
    button = browser.find_element_by_id("verify")
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fillForm(browser)

    finally:
        time.sleep(7)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "http://suninjuly.github.io/wait2.html"
test(link)
