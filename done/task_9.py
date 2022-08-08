from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.select import Select

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num_1 = browser.find_element(By.XPATH, '//*[@id = "num1"]').text
    num_2 = browser.find_element(By.XPATH, '//*[@id = "num2"]').text
    sum_nums = str(int(num_1) + int(num_2))

    print(sum_nums)

    select = Select(browser.find_element(By.XPATH, '//select[@id = "dropdown"]'))

    select.select_by_value(sum_nums)

    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)

# finally:
#     time.sleep(5)
#     browser.quit()
#
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
#
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     num1 = int(browser.find_element(By.ID, "num1").text)
#     num2 = int(browser.find_element(By.ID, "num2").text)
#     Select(browser.find_element(By.ID, "dropdown"))\
#         .select_by_value(str(num2 + num1))
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     #  Выведет в консоль номер решения
#     print(browser._switch_to.alert.text)
#
# finally:
#     sleep(5)
#     browser.quit()