import email
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random import randrange


chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/vasiliskyrillidis/Library/Application Support/Google/Chrome")
driver = webdriver.Chrome(executable_path=r'/Users/vasiliskyrillidis/Desktop/chromedriver',options=options)


driver.get('https://www.buzzsneakers.gr/egrafi')
time.sleep(10)
driver.find_element_by_class_name('cookie-agree-gdpr').click()
time.sleep(4)

i = 0

while i <= 10:

    address = "@beskimi.com"
    random_num = randrange(100000)
    start="Melios"
    new_email = start+str(random_num)+address
    name = "Melios"
    surname = "koutsoumpogeros"

    driver.find_element_by_id('reg_page_firstname').send_keys(name)
    driver.find_element_by_id('reg_page_lastname').send_keys(surname)
    driver.find_element_by_id('reg_page_email').send_keys(new_email)
    driver.find_element_by_id('reg_page_phone').send_keys("6942636851")
    driver.find_element_by_id('reg_page_region_id').send_keys("Ν. ΑΤΤΙΚΗΣ")
    driver.find_element_by_id('reg_page_city').send_keys("Athens")

    time.sleep(5)

    driver.find_element_by_id('reg_page_address').send_keys("Chansen")
    driver.find_element_by_id('reg_page_street_no').send_keys("20")
    driver.find_element_by_id('reg_page_postcode').send_keys("11144")
    driver.find_element_by_id('reg_page_password').send_keys("Bj221777!!")
    driver.find_element_by_id('reg_page_password_repeat').send_keys("Bj221777!!")    

    time.sleep(10)
    
    driver.find_element_by_xpath('//*[@id="registration_page"]/div[2]/div/div[15]/div[1]/div').click()
    
    time.sleep(5)
    
    driver.find_element_by_id('reg_page_submit').click()

    time.sleep(5)
    driver.get('https://www.buzzsneakers.gr/egrafi')