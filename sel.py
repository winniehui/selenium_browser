import datetime
from time import sleep
from selenium import webdriver
import pytest

base_url = "https://pypi.org"



driver = webdriver.Firefox()
driver.get(base_url)
driver.maximize_window()
   
title = driver.title
print ("page title :", title)
sleep(3)
driver.close()



    
