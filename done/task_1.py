# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     driver.get(link)
#
#     input1 = driver.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = driver.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = driver.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = driver.find_element(By.ID, 'country')
#     input4.send_keys("Russia")
#
#     button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
#     button.click()
#     time.sleep(2)
#
# finally:
#
#     time.sleep(5)
#     driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.alert import Alert
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# step_link = "https://stepik.org/lesson/138920/step/4"
# profile_path = 'C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
#
# try:
#     chrome_options = ChromeOptions()
#     chrome_options.add_argument(f'user-data-dir={profile_path}')
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#     alert = Alert(browser)
#     answer = alert.text.split()[-1]
#     time.sleep(3)
#     alert.accept()
#     browser.get(step_link)
#     time.sleep(10)
#     textarea = browser.find_element(By.TAG_NAME, "textarea")
#     textarea.send_keys(answer)
#     time.sleep(2)
#     button = browser.find_element(By.CLASS_NAME, "submit-submission")
#     button.click()
#     time.sleep(3)
#
# finally:
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     input5 = browser.find_element(By.CSS_SELECTOR, "#submit_button")
#     input5.click()
#
# finally:
#     sleep(10)
#     browser.quit()

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Asad")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Umarov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Khujand")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Tajikistan")
    button = browser.find_element_by_css_selector('#submit_button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()