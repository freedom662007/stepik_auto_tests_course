from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
try:
    link = 'http://suninjuly.github.io/file_input.html'
    driver = webdriver.Chrome()
    driver.get(link)
    # заполнить обязательные поля
    firstname = driver.find_element(By.XPATH, ".//form/div/input[@name='firstname']").send_keys('test')
    lastname = driver.find_element(By.XPATH, ".//form/div/input[@name='lastname']").send_keys('test')
    email = driver.find_element(By.XPATH, ".//form/div/input[@name='email']").send_keys('test@test')
    # загрузить файл
    element = driver.find_element(By.ID, 'file')
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test.txt')
    element.send_keys(file_path)
    # нажать кнопку "submit"
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
finally:
    time.sleep(15)
    driver.quit()