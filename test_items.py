import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exist(browser):
    browser.get(link)
    button_add = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    print(f"Text on the button is: {button_add.text}")
    time.sleep(10)
    assert button_add.is_displayed(), "Button for adding to basket is not present"
