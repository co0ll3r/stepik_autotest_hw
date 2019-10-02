from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys("Smolensk@test.com")
    input4 = browser.find_element_by_css_selector('.second_block .first')
    input4.send_keys("+79999999999")
    input5 = browser.find_element_by_css_selector('.second_block .second')
    input5.send_keys("Russia")
    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
