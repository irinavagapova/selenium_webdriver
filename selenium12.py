import pytest
from selenium import webdriver

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
    driver.find_element_by_name("name[en]").send_keys("Flower")
    print('ggg')