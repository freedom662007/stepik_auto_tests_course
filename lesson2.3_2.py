from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver = webdriver.Chrome()
    driver.get(link)
    # Нажать на кнопку
    driver.find_element(By.TAG_NAME, 'button').click()
    # Переключиться на новую вкладку
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    # рассчитать капчу
    x = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    result = calc(x)
    # ввести капчу
    driver.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(result)
    # нажать кнопку 'submit'
    driver.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(15)
    driver.quit()