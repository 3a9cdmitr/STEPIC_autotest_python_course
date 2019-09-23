"""
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ"""


from selenium import webdriver
import time
from function import calc


try:
#1
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/redirect_accept.html')
#2

	browser.find_element_by_tag_name('button').click() 
	time.sleep(1)

#3
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

#4
	x= browser.find_element_by_id('input_value').text
	browser.find_element_by_tag_name('input').send_keys(calc(int(x)))
	
	browser.find_element_by_tag_name('button').click()

#answer_get
	outp = browser.switch_to.alert
	print(outp.text.split()[-1])
	outp.accept()
	time.sleep(2)
	print('')
	print(browser.window_handles)
	browser.switch_to.window(browser.window_handles[0])
	print('')
	print(browser.window_handles)
	time.sleep(2)
	browser.find_element_by_tag_name('button').click() 
	time.sleep(1)
	print('')
	print(browser.window_handles)	
	browser.close()
	print('')
	print(browser.window_handles)

finally:

	
	time.sleep(5)
	browser.quit()
