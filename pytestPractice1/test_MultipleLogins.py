import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import  By
import time


def test_googlelogin():
    driver = webdriver.Chrome("C:\Chrome\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"

def test_FBlogin():
    driver = webdriver.Chrome("C:\Chrome\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"

def test_Instalogin():
    driver = webdriver.Chrome("C:\Chrome\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
# to run all these testcases in parallel mode then we have to use pytest-xdist package
def test_yatralogin():
    driver = webdriver.Chrome("C:\Chrome\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    assert driver.title == "Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com"