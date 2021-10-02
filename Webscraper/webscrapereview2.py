from typing import Text
from emoji.core import emojize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pandas as pd
import emoji

shopee = "https://shopee.ph/JAG-BRANDED-SHIRT-FOR-MEN-(Mall-Pullout)-i.311099315.6853205105"


CO = webdriver.FirefoxOptions()
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe',options=CO)

driver.get(shopee)
driver.implicitly_wait(5)

while True:
    driver.execute_script('window.scrollTo(0,4000);')
    time.sleep(3)
    #scraping product reviews
    prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
    for prod_review in prod_reviews:    
        print(prod_review.text.encode("unicode_escape").decode('utf-8'))
    #scraping product tags
    prod_rating_tags = driver.find_elements_by_class_name('shopee-product-rating__tags')
    for prod_rating_tag in prod_rating_tags:    
        print(prod_rating_tag.text)
        
    right_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[8]')
                                                 
    if right_button:
        while True: 
            right_button.click();
            driver.execute_script('window.scrollTo(0,4000);')                
            time.sleep(3)
            #scraping product reviews
            prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
            for prod_review in prod_reviews:    
                print(prod_review.text.encode("unicode_escape").decode('utf-8'))
            #scraping product tags
            prod_rating_tags = driver.find_elements_by_class_name('shopee-product-rating__tags')
            for prod_rating_tag in prod_rating_tags:    
                print(prod_rating_tag.text)

    else:
        break
driver.close()