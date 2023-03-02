
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = None
def setup_module(module):
    global  driver
    driver = webdriver.Chrome("C:\Chrome\chromedriver.exe")
    driver.implicitly_wait(10)

    driver.get("https://www.facebook.com/")


def teardown_module(module):
    driver.quit()

def test_loginFB ():
    wait= WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element(By.XPATH, "//input[@id = 'email']")).send_keys("8790783061")
    wait.until(EC.text_to_be_present_in_element(By.XPATH,"//input[@id = 'pass']")).send_keys("8790783061")
    wait.until(EC.text_to_be_present_in_element(By.XPATH,"//button[@type = 'submit']")).click()
    account_holder = wait.until(EC.text_to_be_present_in_element(By.XPATH, "/span[contains(text(), 'Find friends')]")).text
    assert account_holder == "Find friends"

