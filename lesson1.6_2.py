# импорт Selenium WebDriver
import time
from selenium import webdriver
# импорт класса By
from selenium.webdriver.common.by import By
import math
try:
    driver = webdriver.Chrome()
    # url страницы
    link = "http://suninjuly.github.io/find_link_text"
    # расчёт значения ссылки
    code = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # открыть страницу
    driver.get(link)
    # кликнуть по ссылке
    driver.find_element(By.LINK_TEXT, code).click()
    # ввести имя
    input1 = driver.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    # ввести фамилию
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    # ввести город
    input3 = driver.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    # ввести страну
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    driver.quit()

