from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    answer=calc(int(browser.find_element_by_id("input_value").text))


    input1=browser.find_element_by_class_name("form-control");
    input1.send_keys(answer)

    check = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check);
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", radio);
    radio.click()








    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # last string