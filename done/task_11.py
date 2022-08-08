
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os



try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input_name = browser.find_element(By.XPATH, '//input[@name = "firstname" and contains(@placeholder, "first")]')
    input_name.send_keys('Andrei')
    input_lstname =  browser.find_element(By.XPATH, '//input[@name = "lastname" and contains(@placeholder, "last")]')
    input_lstname.send_keys('Sad')
    input_email = browser.find_element(By.XPATH, '//input[@name = "email" and contains(@placeholder, "email")]')
    input_email.send_keys('qwerty@tut.by')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'task.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, '//input[@id = "file"]')
    element.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[@type = "submit"]').click()
    print(browser._switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys('file')

#print(os.path.abspath(__file__))
#print(os.path.abspath(os.path.dirname(__file__)))