from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
try:
    # создать драйвер
    driver = webdriver.Chrome()
    # url сайта
    link = 'http://suninjuly.github.io/get_attribute.html'
    # открыть страницу
    driver.get(link)
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    x_1 = driver.find_element(By.ID, 'treasure')
    # найти значение атрибута valuex
    x = x_1.get_attribute('valuex')
    # вычислить значение x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # Ввести ответ в текстовое поле
    driver.find_element(By.ID, 'answer').send_keys(calc(x))
    # Отметить checkbox "I'm the robot"
    driver.find_element(By.ID, 'robotCheckbox').click()
    # Выбрать radiobutton "Robots rule!"
    driver.find_element(By.ID, 'robotsRule').click()
    # Нажать на кнопку "Submit"
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(30)
    driver.quit()