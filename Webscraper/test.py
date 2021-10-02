from typing import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pandas as pd


shopee = 'https://shopee.ph/JAG-BRANDED-SHIRT-FOR-MEN-(Mall-Pullout)-i.311099315.6853205105'


CO = webdriver.FirefoxOptions()
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe',options=CO)

driver.get(shopee)
driver.implicitly_wait(10)


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(4)
    
    prod_rating_tags = driver.find_elements_by_class_name('shopee-product-rating__tags')
    for prod_rating_tag in prod_rating_tags:    
        print(prod_rating_tag.text)
        
    buttons = driver.find_elements_by_class_name('shopee-button-no-outline')
    for button in buttons:    
        print(button.text)
    break;

driver.close()