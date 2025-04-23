from  selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
try:

    link = 'http://suninjuly.github.io/alert_accept.html'
    driver = webdriver.Chrome()
    # Открыть страницу
    driver.get(link)
    # Нажать на кнопку
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    # Принять confirm
    confirm = driver.switch_to.alert
    confirm.accept()
    # получить капчу
    x = driver.find_element(By.ID, 'input_value').text
    # рассчёт формулы
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # ввести результат в поле
    driver.find_element(By.TAG_NAME, 'input').send_keys(calc(x))
    # нажать кнопку 'submit'
    driver.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(15)
    driver.quit()