"""Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from function import calc
import time

try:
#1
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")


	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),'100'))
	browser.find_element_by_id('book').click()
#2
	x= browser.find_element_by_id('input_value').text
	browser.find_element_by_id('answer').send_keys(calc(int(x)))
	
	browser.find_element_by_id('solve').click()
	
	time.sleep(1)
	outp = browser.switch_to.alert
	print(outp.text.split()[-1])
	outp.accept()

	
	
finally:

	
	time.sleep(1)
	browser.quit()

