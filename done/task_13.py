from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link =  "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//div[@class = "container"]//button[contains(@class, "btn")]').click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x_el = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    x = x_el.text
    func = calc(x)
    print(func)
    input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    input_answer.send_keys(func)
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)
    alert = browser._switch_to.alert
    alert.accept()

finally:
    time.sleep(2)
    browser.quit()

    