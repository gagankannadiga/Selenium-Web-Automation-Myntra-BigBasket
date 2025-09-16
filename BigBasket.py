import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import random

from webdriver_manager.core import driver


class BigBasketTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.bigbasket.com/')
        print("Opened BigBasket website")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Closed the browser")


    def test_01_title_verification(self):
        time.sleep(5)
        if "bigbasket" in self.driver.title:
            print("Title verification passed")
        else:
            print("Title verification failed")


    def test_02_search_for_beverages(self):
        time.sleep(5)
        search_box = self.driver.find_element(By.XPATH,"//*[@id=\"siteLayout\"]/header[2]/div[1]/div[1]/div/div/div/div/input")
        search_box.send_keys('Beer')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)
        print("Searched for 'Beverages'")


    def test_03_back_to_home(self):
        time.sleep(5)
        self.driver.back()
        time.sleep(10)
        print("Navigated back to home page")


    def test_04_forward_to_search_results(self):
        time.sleep(5)
        self.driver.forward()
        time.sleep(5)
        print("Navigated forward to search results page")


    def test_05_verify_Beverages_in_title(self):
        time.sleep(5)
        if "Beer" in self.driver.title:
            print("Verified 'Beverages' in title")
        else:
            print("Verification of 'Beverages' in title failed")


    def test_06_scroll_down(self):
        # Scroll down gradually
        scroll_pause_time = 0.5
        screen_height = self.driver.execute_script("return window.innerHeight")
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")

        for i in range(0, scroll_height, screen_height):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)


    def test_07_search_for_ice_cream(self):
        time.sleep(10)
        search_box = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header[1]/div[2]/div[2]/div/div/div/input")
        search_box.send_keys('Ice Cream')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)
        print("Searched for 'Ice Cream'")


    def test_08_verify_Ice_Cream_in_title(self):
        time.sleep(10)
        if "Ice Cream" in self.driver.title:
            print("Verified 'Ice Cream' in title")
        else:
            print("Verification of 'Ice Cream' in title failed")


    def test_09_minimize_browser(self):
        time.sleep(3)
        self.driver.minimize_window()
        time.sleep(3)
        print("Minimized the browser")


    def test_10_maximize_browser(self):
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        print("Maximized the browser")


    def test_11_navigate_to_category_fruits(self):
        time.sleep(10)
        try:
            # Click on the category link (e.g., "Exotic Fruits & Veggies")
            category_link = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[1]/a/div/span')
            category_link.click()

            time.sleep(3)  # Wait for the category page to load

            # Verify the category page is displayed
            category_header = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[1]/a/div/span')
            assert category_header.is_displayed(), "Category page is not displayed"
            print("Navigated to Exotic Fruits & Veggies and verified the page is displayed")
        except NoSuchElementException:
            print("Exotic Fruits & Veggies link or header not found")
        except AssertionError as e:
            print(str(e))

    def test_12_navigate_to_category_tea(self):
        try:
            # Click on the category link (e.g., "Tea")
            category_link = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[2]/a/div/span')
            category_link.click()

            time.sleep(3)  # Wait for the category page to load

            # Verify the category page is displayed
            category_header = self.driver.find_element(By.XPATH,
                                                       '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[2]/a/div/span')
            assert category_header.is_displayed(), "Category page is not displayed"
            print("Navigated to Tea and verified the page is displayed")
        except NoSuchElementException:
            print("Tea link or header not found")
        except AssertionError as e:
            print(str(e))


    def test_13_navigate_to_category_ghee(self):
        time.sleep(10)
        try:
            # Click on the category link (e.g., "Ghee")
            category_link = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[3]/a/div/span')
            category_link.click()

            time.sleep(3)  # Wait for the category page to load

            # Verify the category page is displayed
            category_header = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[3]/a/div/span')
            assert category_header.is_displayed(), "Category page is not displayed"
            print("Navigated to Ghee and verified the page is displayed")
        except NoSuchElementException:
            print("Ghee link or header not found")
        except AssertionError as e:
            print(str(e))


    def test_14_navigate_to_category_nandini(self):
        try:
            # Click on the category link (e.g., "Nandini")
            category_link = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[4]/a/div/span')
            category_link.click()

            time.sleep(3)  # Wait for the category page to load

            # Verify the category page is displayed
            category_header = self.driver.find_element(By.XPATH,
                                                       '/html/body/div[2]/div[1]/header[2]/div[2]/div[2]/ul/li[4]/a/div/span')
            assert category_header.is_displayed(), "Category page is not displayed"
            print("Navigated to Nandini and verified the page is displayed")
        except NoSuchElementException:
            print("Nandini link or header not found")
        except AssertionError as e:
            print(str(e))


    def test_15_scroll_down(self):
        time.sleep(10)
        # Scroll down gradually
        scroll_pause_time = 0.5
        screen_height = self.driver.execute_script("return window.innerHeight")
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")

        for i in range(0, scroll_height, screen_height):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)

        time.sleep(1)
        print("Scrolled down the page gradually")

    def test_16_quit_browser(self):
        time.sleep(5)
        self.driver.quit()
        print("Quit browser")

    def test_17_login(self):
        driver = webdriver.Chrome()
        try:
            driver.get('https://www.bigbasket.com/')

            # Click on the login button
            login_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/header[2]/div[1]/div[2]/div[2]/button')
            login_button.click()

            time.sleep(3)  # Wait for the login modal to appear

            # Enter phone number and proceed
            phone_input = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div/div[2]/form/div/input')
            phone_input.send_keys('9986291940')  # Replace with a valid phone number

            time.sleep(5)

            continue_button = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div/div[2]/form/button')
            continue_button.click()



        finally:
            driver.quit()



    def test_18_page_load_performance(self):
        driver = webdriver.Chrome()
        try:
            start_time = time.time()

            driver.get('https://www.bigbasket.com/')

            end_time = time.time()
            load_time = end_time - start_time
            print(f"Page load time: {load_time} seconds")

            assert load_time < 5, "Page load time is too slow"

        finally:
            driver.quit()

    if __name__ == "_main_":
        
        unittest.main()


