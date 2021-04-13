import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # button2 = browser.find_element_by_tag_name("button")
    # button2.click()
    #
    # time.sleep(1)
    #
    # new_window = browser.window_handles[1];
    # browser.switch_to.window(new_window)
    #
    # input1=browser.find_element_by_class_name("form-control");
    # input1.send_keys(answer)


    button = browser.find_element_by_id("book")
    button.click()

    answer = calc(int(browser.find_element_by_id("input_value").text))
    input1=browser.find_element_by_class_name("form-control");
    input1.send_keys(answer)

    button = browser.find_element_by_id("solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # last string