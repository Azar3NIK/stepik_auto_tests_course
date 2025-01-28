from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    button1.click()
    x_element = browser.find_element(By.ID, 'input_value')
    answer = calc(x_element.text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(answer)
    button1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button1.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла