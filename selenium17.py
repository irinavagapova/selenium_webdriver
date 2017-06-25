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

def test_log(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/")
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    table = driver.find_element_by_css_selector(".dataTable")
    links = table.find_elements_by_css_selector("tr.row td a[title=Edit]")

    for i in range(1,len(links)-1):
        table1 = driver.find_element_by_css_selector(".dataTable")
        link = table1.find_element_by_css_selector("tr.row:nth-child(" + str(i+4) + ") td a[title=Edit]")
        href=link.get_attribute("href")
        link.click()
        driver.implicitly_wait(10)

        for l in driver.get_log("browser"):
            print(l)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        driver.implicitly_wait(10)

