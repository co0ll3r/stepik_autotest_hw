from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
# файл с 2 куками
import cookie_values

# для аутентификации используются 2 куки
# sessionid как cookie_session_val
# csrftoken как cookie_token_val
# в файле cookie_value (смотри последний импорт) 
# есть две переменные session и token соответственно
# это значения этип полей в куке 
cookie_session_val = cookie_values.session
cookie_token_val = cookie_values.token
# ссылка на степ 
step_link = "https://stepik.org/lesson/181384/step/8?unit=156009"

# Рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Данный метод заполняет поля 
def fillForm(browser): 
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button.click()
    x = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_id("solve").click()

# Данный метод копирует ответ в буфер обмена
def getAnswerCode(browser):
    # берем текст ответа
    alert_text = browser.switch_to.alert.text
    # берем код ответа. Спасибо Виталию)
    answer_code = alert_text.split(': ')[-1]
    print(answer_code)

   # если импортнули pyperclip, то данный код скопирует ответ в буфер обмена
   # pyperclip.copy(answer_code)
   # time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    # загружаем ответ на степик
    uploadAnswerToStep(browser, answer_code)

# Загружаем ответ автоматически на степик
# в параметрах: экземпляр драйвера и ответ на задание
def uploadAnswerToStep(browser, answer):
    # вводим куки от сессии
    cookie_session = {'name' : 'sessionid', 'value' : cookie_session_val}
    cookie_token = {'name' : 'csrftoken', 'value' : cookie_token_val}

    # первый раз заходим для закачки куки
    # step_link - глобальная переменнная
    browser.get(step_link)
    # добавляем куки в браузерную сессию
    browser.add_cookie(cookie_session)
    browser.add_cookie(cookie_token)
    # делаем перезаход, т.к. без сессии, сайт редеректит нас на главную
    browser.get(step_link)

    # даём странице время, чтобы загрузиться
    time.sleep(5)
    # вводим ответ и отсылаем
    input_answer = browser.find_element_by_class_name("textarea")
    input_answer.send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    

# Метод в котором осуществляется тестирование
def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fillForm(browser)
        getAnswerCode(browser)

    finally:
        time.sleep(20)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "http://suninjuly.github.io/explicit_wait2.html"
test(link)
