from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()