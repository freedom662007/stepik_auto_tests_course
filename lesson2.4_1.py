from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import math
try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver = webdriver.Chrome()
    driver.get(link)
    # Дождаться, когда цена дома уменьшится до $100
    WebDriverWait(driver, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    # нажать кнопку 'Book'
    driver.find_element(By.ID, 'book').click()
    # получить значение x
    x = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    # рассчитать значение x по формуле
    def calc(num):
        return str(math.log(abs(12 * math.sin(int(x)))))
    result = calc(x)
    # ввести в поле результат рачёта
    driver.find_element(By.ID, 'answer').send_keys(result)
    # нажать кнопку 'Submit'
    driver.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    driver.quit()
