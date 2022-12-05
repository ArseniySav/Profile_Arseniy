from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


name = browser.find_element(By.NAME, "firstname")
name.send_keys("A")
lastname = browser.find_element(By.NAME, "lastname")
lastname.send_keys("A")
email= browser.find_element(By.NAME, "email")
email.send_keys("a")

directory = "C:\chromedriver"
file_name = "file.txt"
file_path = os.path.join(directory, file_name)
element = browser.find_element(By.ID, "file")
element.send_keys(file_path)
button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()