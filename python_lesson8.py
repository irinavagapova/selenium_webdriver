import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_sticker(driver):

    driver.get("http://localhost/litecart/")

    count=driver.find_elements_by_css_selector("#box-most-popular .sticker")
    count_elem=driver.find_elements_by_css_selector("#box-most-popular li.product")
    count1 = driver.find_elements_by_css_selector("#box-campaigns .sticker")
    count_elem1 = driver.find_elements_by_css_selector("#box-campaigns li.product")
    count2 = driver.find_elements_by_css_selector("#box-latest-products .sticker")
    count_elem2 = driver.find_elements_by_css_selector("#box-latest-products li.product")
    print(len(count), len(count_elem))
    print(len(count1), len(count_elem1))
    print(len(count2), len(count_elem2))

    if len(count)==len(count_elem) and len(count1) == len(count_elem1) and len(count2) == len(count_elem2):
        print ('стикеры совпадают с количеством элементов')
    else:
        print('стикеры НЕ совпадают с количеством элементов')



#test_sticker(driver)