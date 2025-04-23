from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math
link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
# окрыть страницу
def driver_get():
    return driver.get(link)
driver_get()
# нажать кнопку Book
def button_click():
    WebDriverWait(driver, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    # нажать кнопку 'Book'
    driver.find_element(By.ID, 'book').click()
button_click()
# получить значение x
def current_x():
    return driver.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
x = current_x()
# рассчитать значение x по формуле
def calc(num):
    return str(math.log(abs(12 * math.sin(int(x)))))
result = calc(x)
# ввести расчёт в поле и нажать кнопку Submit
def enter_in_the_field():
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'solve').click()
enter_in_the_field()
def br_clouse():
    time.sleep(3)
    driver.quit()
br_clouse()


