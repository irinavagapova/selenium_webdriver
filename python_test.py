import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.bing.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("go").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Bing"))