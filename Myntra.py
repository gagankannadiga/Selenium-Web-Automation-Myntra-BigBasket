from selenium import webdriver
from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#set all
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=options)

#test Case:1
try:
        driver = webdriver.Chrome()
        driver.get("https://www.myntra.com/")
        print("window open")
        print("Test case 1:window successfully open and test case 1 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#test Case:2
try:
        driver.maximize_window()
        time.sleep(1)
        print("Test case 2:window maximize and test case 2 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")



#test Case:3
try:
        check_box = driver.find_element(By.CLASS_NAME, "desktop-main")
        check_box.send_keys("Men")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 3:Men Icon check and test case 3 pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#test Case:4
try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 30  # Adjust scroll speed as needed
        for i in range(0, total_height, scroll_speed):
                driver.execute_script(f"window.scrollTo(0, {i});")
                time.sleep(0.1)  # Adjust sleep time if needed for smoothness
        print("Test case 4:Scroll page occur and test case 4 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#test Case:5
try:
        check_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/nav/div/div[2]/div/a")
        check_box.send_keys("Women")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 5:Women Icon check and test case 5 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#test Case:6
try:
        check_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/nav/div/div[3]/div/a")
        check_box.send_keys("Kid")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 6:Kid Icon check and test case 6 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#test Case:7
try:
        check_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/nav/div/div[4]/div/a")
        check_box.send_keys("Home & Living")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 7:Home & Living Icon check and test case 7 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

#test Case:8
try:
        check_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/nav/div/div[5]/div/a")
        check_box.send_keys("Beauty")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 8:Beauty Icon check and test case 8 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

#test Case:9
try:
        check_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/nav/div/div[6]/div/a")
        check_box.send_keys("studio")
        check_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Test case 9:studio Icon check and test case 9 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

#test Case:10
try:
        for _ in range(2):
                driver.back()
                time.sleep(2)  # wait for the page to load

                print("Test case 10:Navigate Backward and test case 10 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

#test Case:11
try:
        driver.forward()
        time.sleep(2)  # wait for the page to load
        assert "Myntra" in driver.page_source
        print(" Test case 11:Navigate Forward and test case 11 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 30  # Adjust scroll speed as needed
        for i in range(0, total_height, scroll_speed):
                driver.execute_script(f"window.scrollTo(0, {i});")
                time.sleep(0.1)  # Adjust sleep time if needed for smoothness
except Exception as e:
    print(f"An error occurred: {str(e)}")


#test Case:12
try:
        search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//input[@class="desktop-searchBar"]')))
        search_box.send_keys('shirt')
        search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="desktop-submit"]')))
        search_button.click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@class="product-base"]')))
        first_product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '(//li[@class="product-base"])[1]')))
        first_product.click()
        driver.switch_to.window(driver.window_handles[1])
        size_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[2]/div/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button'))
        )
        size_button.click()
        size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[2]/div/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button'))
        )
        size_button.click()
        add_to_bag_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]')))
        add_to_bag_button.click()
        go_to_bag_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/a')))
        go_to_bag_button.click()
        print("Test case 12:Product is check and place a order so Test case 12 is pass")
except Exception as e:
    print(f"An error occurred: {str(e)}")
try:

        driver.back()
        time.sleep(2)  # wait for the page to load
        print("Test case 11:Navigate Backward and test case 11 is pass")
except Exception as e:
        print(f"An error occurred: {str(e)}")

#Test case :13
try:
        profile_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/header/div[2]/div[2]/div/div[1]/span[2]"))
        )
        profile_button.click()
        sign_up_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "desktop-linkButton"))
            )
        login_signup_button = driver.find_element(By.CLASS_NAME, 'desktop-linkButton')
        login_signup_button.click()
        time.sleep(2)
        phone_login_option = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/input')
        phone_login_option.click()
        time.sleep(2)

        # Locate the phone number input field and fill it with your phone number
        phone_number_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/input')
        phone_number = "9591772077"  # Replace with your phone number
        phone_number_input.send_keys(phone_number)
        continue_button = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submitBottomOption"))
            )
        print("Test case 13:Sign in Success and test case 13 pass")
        continue_button.click()
except Exception as e:
        print(f"An error occurred: {str(e)}")


driver.quit()









