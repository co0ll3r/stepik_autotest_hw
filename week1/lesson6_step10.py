from selenium import webdriver
import time

# Данный метод заполняет только обязательные поля 
def fillRequirement(browser): 
    value1 = "Input your first name"
    value2 = "Input your last name"
    value3 = "Input your email"
    input1 = browser.find_element_by_css_selector("[placeholder='" + value1 + "']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='" + value2 + "']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='" + value3 + "']")
    input3.send_keys("Smolensk@gmail.com")

# Данный метод заполняет необязательные поля
def fillOptional(browser):
    value1 = "Input your phone:"
    value2 = "Input your address:"
    input1 = browser.find_element_by_css_selector("[placeholder='" + value1 + "']")
    input1.send_keys("88005553535")
    input2 = browser.find_element_by_css_selector("[placeholder='" + value2 + "']")
    input2.send_keys("Luchshe pozvonit chem u kogo to zanimat")

# Метод в котором осуществляется тестирование
def testRegistration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
    #   Вызов метода для заполнения обязательных полей
        fillRequirement(browser)

    #   Метод заполнения необязательных полей 
    #   закомментирован, т.к. не стоит задачи
    #   заполнять необязательные поля
    #   fillOptional()

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        comparison = "Congratulations! You have successfully registered!" == welcome_text
        assert comparison 
        if comparison:
            print("test passed")
    finally:
        time.sleep(10)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
# Тестируем сначала первую ссылку
testRegistration(link1)
testRegistration(link2)

