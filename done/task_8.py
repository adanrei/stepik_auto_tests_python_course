from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, '//img[@id = "treasure"]')
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]').send_keys(y)
    check_box = browser.find_element(By.XPATH, '//input[@id = "robotCheckbox"]').click()
    radio_button = browser.find_element(By.XPATH, '//input[contains(@id, "robotsRule")]').click()
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(x)
    # input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    # input_answer.send_keys(y)
    # option1 = browser.find_element(By.CSS_SELECTOR, "[id = 'robotCheckbox']")
    # option1.click()
    # option2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']")
    # option2.click()
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()