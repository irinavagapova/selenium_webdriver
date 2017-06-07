import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    table = driver.find_element_by_css_selector(".dataTable")
    rows = table.find_elements_by_css_selector("tr.row") # сколько строк
    for i in range(1, len(rows)+1):
        print(i)
        table1 = driver.find_element_by_css_selector(".dataTable")
        table1.find_element_by_css_selector("tr:nth-child(" + str(i+1) + ") a").click() #строки в первой таблице

        table_zone = driver.find_element_by_css_selector("#table-zones") #внутренняя страница
        rows1 = table_zone.find_elements_by_css_selector("tr:not(.header)")
        last_value = ''  # переменная для сравнения
        for r1 in rows1:
            cells1 = r1.find_elements_by_tag_name("td")
            sel = cells1[2].find_elements_by_tag_name("option")
            for s in sel:
                if s.get_attribute('selected'):
                    name_zone=s.get_attribute('innerText')
            if last_value > name_zone:  # если страны не в алфавитном порядке,то вызываем exception
                raise Exception(last_value, ' > ', name_zone)
            print(name_zone, last_value)
            last_value = name_zone

            
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")









