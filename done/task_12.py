from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button[contains(@type, "submit")]').click()
    alert = browser._switch_to.alert
    alert.accept()
    number_x = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    x = number_x.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    solution = calc(x)
    input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    input_answer.send_keys(solution)
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)
    alert = browser._switch_to.alert
    alert.accept()


finally:
    time.sleep(5)
    browser.quit()
