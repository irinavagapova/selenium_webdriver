import pytest
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/create_account")
    driver.find_element_by_name("firstname").send_keys("username"+str(random.randint(1, 1000)))
    driver.find_element_by_name("lastname").send_keys("famname" + str(random.randint(1, 1000)))
    driver.find_element_by_name("address1").send_keys("Leningradskoe highway " + str(random.randint(1, 1000))+"apt."+ str(random.randint(1, 1000)))
    driver.find_element_by_name("postcode").send_keys("140" + str(random.randint(10,99)))
    driver.find_element_by_name("city").send_keys("Moscow")
    Select(driver.find_element_by_name("country_code")).select_by_value("US")
    driver.find_element_by_name("email").send_keys("my_mail" + str(random.randint(1, 1000))+"@mail.ru")
    driver.find_element_by_name("phone").send_keys("+1123456789"+str(random.randint(1, 10)))

    mail =driver.find_element_by_name("email").get_attribute("value")
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, 8):
        id += random.choice(number)
        id += random.choice(alpha)
    driver.find_element_by_name("password").send_keys(id)
    passwd = id
    driver.find_element_by_name("confirmed_password").send_keys(id)
    driver.find_element_by_name("create_account").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Logout").click()
    driver.implicitly_wait(10)
    log_f=driver.find_element_by_css_selector("#box-account-login")
    #print(mail)
    log_f.find_element_by_name("email").send_keys(mail)
    log_f.find_element_by_name("password").send_keys(passwd)
    log_f.find_element_by_name("login").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Logout").click()
    driver.implicitly_wait(10)
    #print(id)

