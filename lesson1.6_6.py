from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    # Ваш код, который заполняет обязательные поля
    first_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys('ivan')
    last_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys('ivanov')
    user_email = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys('test@test')
 # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()