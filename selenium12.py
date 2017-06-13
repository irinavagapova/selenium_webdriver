import pytest
from selenium import webdriver
import urllib.request
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_link_text("Add New Product").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
    driver.find_element_by_name("name[en]").send_keys("Cat")

    urllib.request.urlretrieve("https://raw.githubusercontent.com/irinavagapova/selenium_webdriver/master/cat.jpg", "D:\\cat.jpg")
    driver.find_element_by_name("new_images[]").send_keys("D:\\cat.jpg")

    tab=driver.find_element_by_css_selector("div.tabs")
    tab.find_element_by_link_text("Information").click()
    driver.implicitly_wait(10)
    Select(driver.find_element_by_name("manufacturer_id")).select_by_value("1")
    driver.find_element_by_name("short_description[en]").send_keys("Black funny Cat")

    tab.find_element_by_link_text("Prices").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("purchase_price").send_keys(Keys.HOME + "1")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value("USD")

    driver.find_element_by_name("save").click()
    driver.implicitly_wait(10)

    

