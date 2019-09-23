"""
открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""

from selenium import webdriver
import time
import os

try:
#1
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")
#2
	input1 = browser.find_element_by_name('firstname')
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_name('lastname')
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_name('email')
	input3.send_keys("Smolensk@mail")
#3
	send_file= browser.find_element_by_name('file')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file_to_get.txt') 
	send_file.send_keys(file_path)	
#4
	button = browser.find_element_by_tag_name('button')
	button.click()




finally:
	time.sleep(4)
	browser.quit()













