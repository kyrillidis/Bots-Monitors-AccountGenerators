from webdriver_manager.chrome import ChromeDriverManager
from webbrowser import BaseBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

import csv
import random
import time
import os
import sys

from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from turtle import delay

name_list=[]
surname_list=[]
email_list=[]
mobilephone_list=[]
country_list=[]
address_list=[]
city_list=[]
post_code_list=[]
size_list=[]
country_list=[]
state_list=[]

cardnumber_list=[]
expmonthlist=[]
expyearlist=[]
cvvlist=[]

filename = open('/Users/vasiliskyrillidis/Desktop/jd sports/profiles.csv', 'r')#, encoding='utf-8')

file = csv.DictReader(filename)

for col in file:
    email_list.append(col['email'])
    name_list.append(col['name'])
    surname_list.append(col['surname'])
    mobilephone_list.append(col['mobile phone'])
    size_list.append(col['size'])
    country_list.append(col['country'])
    address_list.append(col['address'])
    city_list.append(col['city'])
    post_code_list.append(col['zip code'])
    state_list.append(col['state'])
    cardnumber_list.append(col['card number'])
    expmonthlist.append(col['expiration month'])
    expyearlist.append(col['expiration year'])
    cvvlist.append(col['cvv'])


#s=Service(ChromeDriverManager().install())
#browser = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/vasiliskyrillidis/Library/Application Support/Google/Chrome")
browser = webdriver.Chrome(executable_path=r'/Users/vasiliskyrillidis/Desktop/raffle bot slamdunk/chromedriver', options=options)

for i in range(len(name_list)):
    browser.get('https://raffle.jdsports.gr/products/nike-dunk-low-panda-w')
    wait = WebDriverWait(browser, 40)
    browser.maximize_window()
    try:
     cookies=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[5]/div[2]/a[2]")))
     browser.execute_script("arguments[0].click();", cookies)
    except:
        pass

    size_but = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-select-2-input']")))
    size_but=browser.find_element(By.XPATH,"//*[@id='react-select-2-input']")
    time.sleep(5)
    size_but.send_keys(size_list[i])
    browser.find_element(By.XPATH,"//*[@id='react-select-2-input']").send_keys(Keys.RETURN)
    time.sleep(2)
    enter_raffle_but=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    browser.execute_script("arguments[0].click();", enter_raffle_but)
    time.sleep(5)


    email=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='email']")))
    email=browser.find_elements(By.XPATH,"//*[@type='email']")[-1]
    email.send_keys(email_list[i])
    time.sleep(10)

    letsgo=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    letsgo=browser.find_elements(By.XPATH,"//*[@type='submit']")[-1]
    browser.execute_script("arguments[0].click();", letsgo)
    time.sleep(5)

    ship=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="delivery"]/div/div[2]/div[1]')))
    ship=browser.find_element(By.XPATH,'//*[@id="delivery"]/div/div[2]/div[1]')
    browser.execute_script("arguments[0].click();", ship)
    time.sleep(5)

    last_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΕΠΙΘΕΤΟ']")))
    last_name=browser.find_element(By.XPATH,"//*[@placeholder='ΕΠΙΘΕΤΟ']")
    last_name.send_keys(surname_list[i])
    time.sleep(1)

    first_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΟΝΟΜΑ']")))
    first_name=browser.find_element(By.XPATH,"//*[@placeholder='ΟΝΟΜΑ']")
    first_name.send_keys(name_list[i])
    time.sleep(2)

    phone=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='tel']")))
    phone=browser.find_element(By.XPATH,"//*[@type='tel']")
    phone.send_keys(mobilephone_list[i])
    time.sleep(1)

    city=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΠΟΛΗ']")))
    city=browser.find_element(By.XPATH,"//*[@placeholder='ΠΟΛΗ']")
    city.send_keys(city_list[i])
    time.sleep(1)

    address=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΔΙΕΥΘΥΝΣΗ']")))
    address=browser.find_element(By.XPATH,"//*[@placeholder='ΔΙΕΥΘΥΝΣΗ']")
    address.send_keys(address_list[i])
    time.sleep(1)

    zip=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='TK']")))
    zip=browser.find_element(By.XPATH,"//*[@placeholder='TK']")
    zip.send_keys(post_code_list[i])
    time.sleep(1)

    country = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-select-4-input']")))
    country=browser.find_element(By.XPATH,"//*[@id='react-select-4-input']")
    time.sleep(2)
    country.send_keys(country_list[i])
    browser.find_element(By.XPATH,"//*[@id='react-select-4-input']").send_keys(Keys.RETURN)
    time.sleep(2.5)
    if country_list[i] == 'Ελλάδα':
        state = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-select-5-input']")))
        state=browser.find_element(By.XPATH,"//*[@id='react-select-5-input']")
        time.sleep(2)
        state.send_keys('ΑΤΤΙΚΗΣ')
        browser.find_element(By.XPATH,"//*[@id='react-select-5-input']").send_keys(Keys.RETURN)
    time.sleep(2)

    letsgo2=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    letsgo2=browser.find_elements(By.XPATH,"//*[@type='submit']")[-1]
    browser.execute_script("arguments[0].click();", letsgo2)
    time.sleep(5)

    debitcard=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='radio-label']")))
    debitcard=browser.find_element(By.XPATH,"//*[@class='radio-label']")
    browser.execute_script("arguments[0].click();", debitcard)
    time.sleep(3)

    payment=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    payment=browser.find_element(By.XPATH,"//*[@type='submit']")
    browser.execute_script("arguments[0].click();", payment)

    time.sleep(20)


    cardholder=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardHolder']")))
    cardholder=browser.find_element(By.XPATH,"//*[@name='cardHolder']")
    browser.execute_script("arguments[0].click();", cardholder)
    cardnumber=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardNumber']")))
    cardnumber=browser.find_element(By.XPATH,"//*[@name='cardNumber']")
    cardnumber.send_keys(cardnumber_list[i])
    cardexp=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardExpiration']")))
    cardexp=browser.find_element(By.XPATH,"//*[@name='cardExpiration']")
    cardexp.send_keys(expmonthlist[i])
    cardcvv=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardCvv']")))
    cardcvv=browser.find_element(By.XPATH,"//*[@name='cardCvv']")
    cardcvv.send_keys(expyearlist[i])
    paybutton=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pay-btn-amount']")))
    paybutton=browser.find_element(By.XPATH,"//*[@id='pay-btn-amount']")