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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    table=driver.find_element_by_css_selector(".dataTable")
    rows=table.find_elements_by_css_selector("tr.row")
    last_value='' # переменная для сравнения
    i=1+1 # пропуск header таблицы
    arr_zone=[]
    for row in rows:
        cells=row.find_elements_by_tag_name("td")
        country=cells[4].get_attribute("innerText")
        zone=cells[5].text
        if last_value > country:  #если страны не в алфавитном порядке,то вызываем exception
            raise Exception(last_value,' > ', country)
        if int(zone) > 0:
            arr_zone.append(i)  #запоминаем номера зон!=0
        #print(country, last_value)
        last_value=country
        i+=1

    print(arr_zone)

    for z in arr_zone:
        table1 = driver.find_element_by_css_selector(".dataTable")
        rows_zone=table1.find_element_by_css_selector("tr:nth-child(" + str(z) + ") a").click() #строки в первой таблице
        table_zone=driver.find_element_by_css_selector("#table-zones")
        rows1 = table_zone.find_elements_by_css_selector("tr.row")
        last_value1 = ''  # переменная для сравнения
        for row1 in rows1:
            cells1 = row1.find_elements_by_tag_name("td")
            name_zone = cells[2].get_attribute("innerText")
            if last_value1 > name_zone:  # если страны не в алфавитном порядке,то вызываем exception
                raise Exception(last_value1, ' > ', name_zone)
            print(name_zone, last_value1)
            last_value1 = name_zone

        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")








