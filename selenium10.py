import pytest
from selenium import webdriver
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox()
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/")
    name_main=driver.find_element_by_css_selector("#box-campaigns .name").get_attribute("innerText")
    camp_price_main=driver.find_element_by_css_selector("#box-campaigns .campaign-price").get_attribute("innerText")
    reg_price_main = driver.find_element_by_css_selector("#box-campaigns .regular-price").get_attribute("innerText")

    camp_price_color_main = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("color")
    hex_cmc=Color.from_string(camp_price_color_main).hex
    reg_price_color_main = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("color")
    hex_rpc=Color.from_string(reg_price_color_main).hex

    camp_price_font_main = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-size")
    reg_price_font_main = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("font-size")

    driver.find_element_by_css_selector("#box-campaigns a.link").click()
    driver.implicitly_wait(10) #неявное ожидание
    name_inner = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")
    camp_price_inner = driver.find_element_by_css_selector(".information .campaign-price").get_attribute("innerText")
    reg_price_inner = driver.find_element_by_css_selector(".information .regular-price").get_attribute("innerText")

    camp_price_color_inner = driver.find_element_by_css_selector(".information .campaign-price").value_of_css_property("color")
    hex_cpi=Color.from_string(camp_price_color_inner).hex
    reg_price_color_inner = driver.find_element_by_css_selector(".information .regular-price").value_of_css_property("color")
    hex_rpi=Color.from_string(reg_price_color_inner).hex

    camp_price_font_inner = driver.find_element_by_css_selector(".information .campaign-price").value_of_css_property("font-size")
    reg_price_font_inner = driver.find_element_by_css_selector(".information .regular-price").value_of_css_property("font-size")
    if name_main != name_inner:  # если назвния не совпадают,то вызываем exception
        raise Exception(name_main, ' != ', name_inner)
    elif camp_price_main != camp_price_inner:
        raise Exception(camp_price_main, ' != ', camp_price_inner)
    elif reg_price_main != reg_price_inner:
        raise Exception(reg_price_main, ' != ', reg_price_inner)
    elif camp_price_font_main < reg_price_font_main:
        raise Exception(camp_price_font_main, ' < ', reg_price_font_main)
    elif camp_price_font_inner < reg_price_font_inner:
        raise Exception(camp_price_font_inner, ' < ', reg_price_font_inner)
    elif hex_cmc[3]!='0' or hex_cmc[4]!='0' or hex_cmc[5]!='0' or hex_cmc[6]!='0':
        raise Exception(camp_price_color_main, ' не красный! ')
    elif hex_cpi[3]!='0' or hex_cpi[4]!='0' or hex_cpi[5]!='0' or hex_cpi[6]!='0':
        raise Exception(camp_price_color_inner, ' не красный! ')
    elif hex_rpc[1:3]!=hex_rpc[3:5]!=hex_rpc[5:] :
        raise Exception(reg_price_color_main, ' не серый! ')
    elif hex_rpi[1:3]!=hex_rpi[3:5]!=hex_rpi[5:] :
        raise Exception(reg_price_color_inner, ' не серый! ')


    print(hex_cmc)
    print(hex_cpi)
    print(hex_rpc)
    print(hex_rpi)
    print(hex_cmc[1:3])
    print(hex_cmc[3:5])
    print(hex_cmc[5:])
    print(name_main, name_inner)
    print(camp_price_main,camp_price_inner)
    print(reg_price_main,reg_price_inner)
    print(camp_price_color_main,camp_price_color_inner)
    print(reg_price_color_main,reg_price_color_inner)
    print(camp_price_font_main,camp_price_font_inner)
    print(reg_price_font_main,reg_price_font_inner)