import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver,args):
    try:
        driver.find_element_by_css_selector(args)
        return True
    except NoSuchElementException:
        return False

def is_text_present(driver,args):
    try:
        driver.find_element_by_css_selector(args)
        return True
    except NoSuchElementException:
        return False

def test_example(driver):
    wait=WebDriverWait(driver, 20)
    driver.get("http://localhost/litecart/")
    for i in range(1,4):
        driver.find_element_by_css_selector("#box-most-popular ul li a").click()
        if is_element_present(driver,".buy_now select"):
            Select(driver.find_element_by_name("options[Size]")).select_by_value("Small")

        element =wait.until(EC.element_to_be_clickable((By.NAME, "add_cart_product")))
        element.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#cart span.quantity"),str(i)))
        driver.get("http://localhost/litecart/")

    driver.find_element_by_link_text("Checkout »").click()
    wait.until(EC.title_is(("Checkout | My Store")))

    for j in range(1, i+1):
        if is_text_present(driver,"#checkout-cart-wrapper em"): #ведем удаление элементов пока не появится текст There are no items in your cart.
            break
        else:
             product=wait.until(EC.element_to_be_clickable((By.NAME, "remove_cart_item")))
             product.click()
             driver.implicitly_wait(3)


