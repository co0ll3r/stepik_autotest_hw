from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
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
step_link = "https://stepik.org/lesson/184253/step/6?unit=158843"

# Рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Данный метод заполняет поля 
def fillForm(browser): 
    browser.find_element_by_class_name("trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value1 = "input_value"
    value2 = "answer"
    value5 = "[type='submit']"
    x = calc(browser.find_element_by_id(value1).text)
    input1 = browser.find_element_by_id(value2)
    input1.send_keys(x)
    button = browser.find_element_by_tag_name("button")
    button.click()
    getAnswerCode(browser)

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

    finally:
        time.sleep(20)
        print("closing browser")
        browser.quit()

# Главный метод (точка входа)
link = "http://suninjuly.github.io/redirect_accept.html"
test(link)
