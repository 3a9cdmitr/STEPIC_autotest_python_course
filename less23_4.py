"""ткрыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом"""

from selenium import webdriver
import time


from function import calc


try:
#1
	browser=webdriver.Chrome()
	browser.get('http://suninjuly.github.io/alert_accept.html')
#2

	browser.find_element_by_tag_name('button').click() 

#3
	browser.switch_to.alert.accept()
#	confirm.accept()     #browser.switch_to.alert.accept() 
#4
	x= browser.find_element_by_id('input_value').text
	browser.find_element_by_tag_name('input').send_keys(calc(int(x)))
	#answ.send_keys(calc(int(x)))

	browser.find_element_by_tag_name('button').click()

#answer_get
	outp = browser.switch_to.alert
	print(outp.text.split()[-1])
	outp.accept()
finally:

	
	time.sleep(2)
	browser.quit()
