from typing import Text
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pandas as pd
products= []






shopee = "https://shopee.ph/Face-mask-holder-Lanyard-for-face-mask-strap-chain-necklace-Pearl-Eyeglasses-Lanyards-Neck-Hanging-R-i.423714846.9664845009?sp_atk=c6a4b0cc-5df0-4fdc-8fe3-4e26169042d8"

rating = []


CO = webdriver.FirefoxOptions()
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe',options=CO)
driver.get(shopee)
driver.implicitly_wait(7)

i = 1

while True:
    solid_button = driver.find_element_by_class_name('shopee-button-solid--primary ')
    if int(solid_button.text)== 1:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(4)
    
        prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
        for prod_review in prod_reviews:
            print(prod_review.text.encode('unicode_escape').decode('utf-8'))
            product = {'Product_Reviews': prod_review.text}
            products.append(product)

           
    if int(solid_button.text)!= i:
        break;
        
    right_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button[8]')
    if right_button:
        while True: 
                i = i+1
                right_button.click();
                solid_button = driver.find_element_by_class_name('shopee-button-solid--primary ')
                if int(solid_button.text)== i:
                    solid_button = driver.find_element_by_class_name('shopee-button-solid--primary ')
                    driver.execute_script('window.scrollTo(0,4000);')                
                    time.sleep(3)
                    prod_reviews = driver.find_elements_by_class_name('shopee-product-rating__content')
                    for prod_review in prod_reviews:
                        print(prod_review.text.encode('unicode_escape').decode('utf-8'))
                        product = {'Product_Reviews': prod_review.text}
                        products.append(product)

                if int(solid_button.text) != i:
                    break;
    
    break;
df = pd.DataFrame(products, columns = ['Product_Name','Product_Reviews'])
            
df.to_csv('C:/Users/johnr/Documents/Thesis Coding/Webscraper/jeremy.csv',columns=['Product_Reviews'],index = False, encoding = 'utf-8')

driver.close()