from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def quit(self):
        self.driver.quit()

    def open_page(self,url):
        self.driver.get(url)

    def code_page(self):
        self.driver.find_element_by_id("enter").click()
        self.wait.until(EC.presence_of_element_located((By.NAME, "robot")))
        secret_value = self.driver.find_element_by_name("secret")
        self.driver.execute_script("arguments[0].setAttribute('type',' ');", secret_value)  # hidden element became visible
        self.wait.until(EC.visibility_of_element_located((By.NAME, "secret")))
        secret = self.driver.find_element_by_name("secret").get_attribute("value")
        self.driver.find_element_by_name("code").send_keys(secret)
        # checking is checkbox selected
        if self.driver.find_element_by_name("robot").is_selected():
            self.driver.find_element_by_css_selector("button[type=submit]").click()
        else:
            self.driver.find_element_by_name("robot").click()
            self.driver.find_element_by_css_selector("button[type=submit]").click()

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul")))  # waiting list

    def verify_list_total(self):
        # verify that all the categories and their quotes are displayed
        with open("quotes.txt") as file:
            array_file = [row.strip() for row in file]  # array static from file

        list_quotes = self.driver.find_element_by_css_selector("ul")
        list_quotes_text = list_quotes.text
        list_quotes_arr = list_quotes_text.split("\n")
        arr_num = list()  # arrayof numbers of quotes
        arr_text = list()  # array list quotes from web page
        for str_q in list_quotes_arr:
            arr = str_q.split(' (')
            arr_text.append(arr[0])
            if len(arr) > 1:
                arr_num.append(int(arr[1].replace(")", "")))
        arr_text.sort()
        array_file.sort()
        assert (arr_text == array_file), "The categories and their quotes not equal"

        # verify that the "Total score:" is the sum of all quote scores
        total_quot_sum = sum(arr_num)
        total_wp = self.driver.find_element_by_css_selector("body")
        total_score_wp = int(total_wp.text.split("Total score: ")[1])
        assert (total_score_wp == total_quot_sum), "Total score isn't the sum of all quote scores"

