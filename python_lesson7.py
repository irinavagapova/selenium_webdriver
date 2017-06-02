import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    # смотрим сколько элементов в главном меню
    links=driver.find_elements_by_css_selector("#box-apps-menu a")

    for i in range(1,len(links)+1):
        driver.find_element_by_css_selector("#box-apps-menu li:nth-child(" + str(i) + ") a").click()
        print(i)

        if is_element_present(driver, By.CSS_SELECTOR, "#box-apps-menu ul.docs a") == True:

            sub_links = driver.find_elements_by_css_selector("#box-apps-menu ul.docs a")

            for j in range(1,len(sub_links)+1):
                driver.find_element_by_css_selector("#box-apps-menu ul.docs li:nth-child(" + str(j) + ") a").click()
                wait1 = WebDriverWait(driver, 10)
                sub_element = wait1.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
                print(sub_element)
        else:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))


  #  print (driver.getcurrent_url())




