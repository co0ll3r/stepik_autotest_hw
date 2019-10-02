from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Запоняем обязатеьные поля
    input1 = browser.find_element_by_css_selector(".first_block .form-group.first_class .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .form-group.second_class .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .form-group:nth-child(3) .form-control.third")
    input3.send_keys("test@test.test")
    # Отпраляем форму
    buttton = browser.find_element_by_css_selector("button.btn")
    buttton.click()

    # Проверяем, что смогли зарегистрировать
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    # записываем в переменную велкомк
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()



