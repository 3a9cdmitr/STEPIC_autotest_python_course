"""Ваша программа должна выполнить следующие шаги:
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x= browser.find_element_by_id('input_value').text
    y=calc(int(x))
    print(y)

    answ = browser.find_element_by_id('answer')
    answ.send_keys(y)

    browser.execute_script("return arguments[0].scrollIntoView(true);", answ)
    
    
        
    
    chek = browser.find_element_by_id('robotCheckbox')
    chek.click()
    

    radiob = browser.find_element_by_id('robotsRule')
    radiob.click()

    button = browser.find_element_by_tag_name("button")   
    button.click() 

    #time.sleep(5)
    outp = browser.switch_to.alert
    print(outp.text)

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
