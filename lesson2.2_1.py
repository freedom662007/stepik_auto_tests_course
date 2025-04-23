from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = 'http://suninjuly.github.io/selects2.html'
    driver = webdriver.Chrome()
    # Открыть страницу
    driver.get(link)
    # найти первое число
    num_1 = driver.find_element(By.ID, 'num1').text
    # найти второе число
    num_2 = driver.find_element(By.ID, 'num2').text
    # найти сумму
    sum_num = int(num_1) + int(num_2)
    # присвоить переменной sum_num тип строка
    sum = str(sum_num)
    # найти список
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    # Выбрать в выпадающем списке значение равное расчитанной сумме, по видимому тексту
    select.select_by_visible_text(sum)
    # Нажать кнопку "Submit"
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(30)
    driver.quit()