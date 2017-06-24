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

def test_window(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logotype")))
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_link_text("Add New Country").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "H1"), "Add New Country"))
    a_href=driver.find_elements_by_css_selector("form a[target=_blank]")

    for  a_i in a_href:
        main_window = driver.current_window_handle
        old_windows = driver.window_handles #список текущих окон
        a_i.click()
        wait.until(lambda driver: len(old_windows) != len(driver.window_handles))
        new_window=driver.window_handles[1]
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
        print("main_window="+main_window,"new_window="+new_window)
