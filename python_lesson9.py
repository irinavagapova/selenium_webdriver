import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    table=driver.find_element_by_css_selector(".dataTable")
    rows=table.find_elements_by_tag_name("tr")
    for row in rows:
        cells=row.find_elements_by_tag_name("td")
        country=cells[4].get_attribute("innerText")
        print(country)
        






