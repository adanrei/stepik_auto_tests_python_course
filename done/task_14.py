import time

import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id = 'price']"), '$100')
    )
    button = browser.find_element(By.XPATH, '//button[@id = "book"]')
    button.click()
    button = browser.find_element(By.XPATH, "//button[@id = 'solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    x = browser.find_element(By.XPATH, '//span[@id = "input_value"]').text
    function_math = calc(x)
    
    print(function_math)
    
    input_answer = browser.find_element(By.XPATH, '//input[@id = "answer"]')
    input_answer.send_keys(function_math)
    
    button = browser.find_element(By.XPATH, '//button[@id = "solve"]').click()
    print(browser._switch_to.alert.text)

finally:
    # time.sleep(2)
    browser.quit()

