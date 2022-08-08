from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "https://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)
    #scroll
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    #browser.execute_script("window.scrollBy(0, 120);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #input
    input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    input_answer.send_keys(y)
    browser.execute_script("window.scrollBy(0, 120);")
    #browser.execute_script("window.scrollBy(0, 120);")
    check_box = browser.find_element(By.XPATH, '//input[@id = "robotCheckbox"]').click()
    radio_button = browser.find_element(By.XPATH, '//input[contains(@id, "robotsRule")]').click()
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()





button = browser.find_element(By.TAG_NAME, "button")
button.click()