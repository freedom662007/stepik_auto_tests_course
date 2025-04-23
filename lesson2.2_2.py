import math
import time
from selenium import webdriver
# импорт класса By
from selenium.webdriver.common.by import By
link = 'https://suninjuly.github.io/execute_script.html'
driver = webdriver.Chrome()
driver.get(link)
num = driver.find_element(By.ID, 'input_value')
x_1 = num.text
x = int(x_1)
def code(x):
    return math.log(abs(12*math.sin(x)))
result_1 = code(x)
result = str(result_1)
# ввести текст в поле
driver.find_element(By.ID, 'answer').send_keys(result)
# проскролить страницу
driver.execute_script("window.scrollBy(0, 100);")
# включить чек-бокс  "I'm the robot"
button_checkbox = driver.find_element(By.ID, 'robotCheckbox')
button_checkbox.click()
# Переключить radiobutton "Robots rule!"
radiobutton = driver.find_element(By.ID, 'robotsRule')
radiobutton.click()
# Нажать на кнопку "Submit"
button = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()
time.sleep(20)
driver.quit()