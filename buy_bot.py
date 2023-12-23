from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])  
options.add_experimental_option("useAutomationExtension", False) 

driver = webdriver.Chrome() 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def openBrowser():
    driver.get("https://www.zara.com/nl/")

def continue_ned():
    time.sleep(5)
    #this is here only if you are using a different zara website (not your local one)
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/section[1]/button[1]").click()
    except:
        pass

def get_to_login_page():
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/header/div[3]/a[1]").click()

def login():
    time.sleep(5)
    username_input = driver.find_element(By.ID, "logonId51")
    password_input = driver.find_element(By.ID, "password55")
    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div[2]/main/article/div/div[2]/div/div[1]/section/form/div[2]/button")

    username_input.send_keys("<Your Email>")
    password_input.send_keys("<Your Password>")

    login_button.click()

def main():
    openBrowser()
    continue_ned()
    get_to_login_page()
    login()
    time.sleep(500000000)

main()
