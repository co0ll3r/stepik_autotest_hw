from selenium import webdriver
import time

# Данный метод заполняет поля 
def fillForm(browser): 
    browser.execute_script("return alert('Start')")
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.dismiss()
    browser.execute_script("return confirm('Wann cookies?')")
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    browser.execute_script("return prompt('INPUT SMTH?')")
    time.sleep(1)
    alert = browser.switch_to.alert


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

