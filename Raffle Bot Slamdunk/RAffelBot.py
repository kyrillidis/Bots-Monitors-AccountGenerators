from lib2to3.pgen2 import driver
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import csv
data=[]
rang=[]
# size=input("D:")
i=0
with open('csv form.csv') as file_obj:
  
    reader_obj = csv.reader(file_obj)
      
    for row in reader_obj:
        data.append(row)
        i+=1
        print(row)
    rang.append(i)
    print(i)
chrome_options = Options()

S=Service(ChromeDriverManager().install())


browser = webdriver.Chrome(service=S,options=chrome_options)

j=1

while(j<i):


    browser.get('https://raffle.slamdunk.gr/products/jordan-1-high-og')
    wait = WebDriverWait(browser, 60)
    browser.maximize_window()
    try:
     cookies=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[5]/div[2]/a[2]")))
     browser.execute_script("arguments[0].click();", cookies)
    except:
        pass

    size_but = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-select-2-input']")))
    size_but=browser.find_element(By.XPATH,"//*[@id='react-select-2-input']")
    time.sleep(5)
    size_but.send_keys(data[j][1])
    browser.find_element(By.XPATH,"//*[@id='react-select-2-input']").send_keys(Keys.RETURN)
    enter_raffle_but=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    # browser.execute_script("arguments[0].click();", enter_raffle_but)
    time.sleep(5)
    enter_raffle_but.click()
    email=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='email']")))
    email=browser.find_elements(By.XPATH,"//*[@type='email']")[-1]
    email.send_keys(data[j][0])
    time.sleep(30)
    letsgo=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    letsgo=browser.find_elements(By.XPATH,"//*[@type='submit']")[-1]
    # browser.execute_script("arguments[0].click();", letsgo)
    letsgo.click()
    ship=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='button-title']")))
    ship=browser.find_element(By.XPATH,"//*[@class='button-title']")
    # browser.execute_script("arguments[0].click();", ship)
    time.sleep(5)

    ship.click()

    last_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΕΠΙΘΕΤΟ']")))
    last_name=browser.find_element(By.XPATH,"//*[@placeholder='ΕΠΙΘΕΤΟ']")
    last_name.send_keys(data[j][3])
    first_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@placeholder='ΟΝΟΜΑ']")))
    first_name=browser.find_element(By.XPATH,"//*[@placeholder='ΟΝΟΜΑ']")
    first_name.send_keys(data[j][2])
    phone=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='tel']")))
    phone=browser.find_element(By.XPATH,"//*[@type='tel']")
    phone.send_keys(data[2][-2])
    store=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-select-3-input']")))
    store=browser.find_element(By.XPATH,"//*[@id='react-select-3-input']")
    store.send_keys("ATTIKH")
    browser.find_element(By.XPATH,"//*[@id='react-select-3-input']").send_keys(Keys.RETURN)
    enter=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    enter=browser.find_element(By.XPATH,"//*[@type='submit']")
    # browser.execute_script("arguments[0].click();", enter)
    time.sleep(5)

    enter.click()
    # warning=browser.find_element(By.XPATH,"")
    debitcard=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='radio-label']")))
    debitcard=browser.find_element(By.XPATH,"//*[@class='radio-label']")
    browser.execute_script("arguments[0].click();", debitcard)
    payment=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    payment=browser.find_element(By.XPATH,"//*[@type='submit']")
    browser.execute_script("arguments[0].click();", payment)
    cardholder=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardHolder']")))
    cardholder=browser.find_element(By.XPATH,"//*[@name='cardHolder']")
    browser.execute_script("arguments[0].click();", cardholder)
    cardnumber=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardNumber']")))
    cardnumber=browser.find_element(By.XPATH,"//*[@name='cardNumber']")
    cardnumber.send_keys(data[j][-5])
    cardexp=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardExpiration']")))
    cardexp=browser.find_element(By.XPATH,"//*[@name='cardExpiration']")
    cardexp.send_keys(data[j][-4])
    cardcvv=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='cardCvv']")))
    cardcvv=browser.find_element(By.XPATH,"//*[@name='cardCvv']")
    cardcvv.send_keys(data[j][-4])
    paybutton=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pay-btn-amount']")))
    paybutton=browser.find_element(By.XPATH,"//*[@id='pay-btn-amount']")
    time.sleep(5)
    browser.execute_script("arguments[0].click();", paybutton)
    # wait1=wait.until(EC.element_to_be_clickable((By.TAG_NAME,"iframe")))
    # w=wait.until(EC.element_to_be_clickable((By.TAG_NAME,"iframe")))
    # browser.switch_to.frame(browser.find_element(By.XPATH,"//input[@value='CONTINUE']"))
    # contin_butt=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='CONTINUE']")))
    # time.sleep(10)
    try:
      time.sleep(20)

      contin_butt=browser.find_element(By.XPATH,"//input[@value='CONTINUE']")
    except:
        time.sleep(20)

        pass
    # print(contin_butt)
    # contin_butt.click()
    # browser.execute_script("arguments[0].click();", contin_butt)
    # time.sleep(10)

    j+=1