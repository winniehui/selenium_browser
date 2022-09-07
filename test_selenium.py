
import datetime
from time import sleep
from selenium import webdriver
import pytest

##url = "https://pypi.org"

test_title = "PyPI · The Python Package Index"

## pytest test_selenium.py --browser firefox --url https://pypi.org


def test_me(request):
    browser_type = request.config.getoption("--browser")
    base_url =  request.config.getoption("--url")
    if browser_type == "firefox" :
       driver = webdriver.Firefox()
    elif browser_type == "chrome": 
        driver =  webdriver.Chrome()


    driver.get(base_url)
      
    title = driver.title
    print ("page title :", title)
    assert title == test_title
    sleep(1)
    driver.close()

