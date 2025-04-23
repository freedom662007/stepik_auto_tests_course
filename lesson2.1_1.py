from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
try:
    driver = webdriver.Chrome()
    link = 'https://suninjuly.github.io/math.html'
    driver.get(link)
    x = driver.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    print(calc(x))
    driver.find_element(By.ID, 'answer').send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(10)
    driver.quit()

