from time import sleep
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://app.psw.gov.pk/app/')
sleep(5)
Id_box = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/fieldset/div/div[1]/input')
Pass_box = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/fieldset/div/div[2]/input')

with open('bot.txt','r') as handle:
        creds = handle.readlines()
Id = creds[0]
Pass = creds[1]
Id_box.send_keys(Id)
Id_box.send_keys(Keys.RETURN)
Pass_box.send_keys(Pass)
Pass_box.send_keys(Keys.RETURN)
sleep(1)
#driver.get('https://www.adidas.com/us/superstar-shoes/EG4959.html?pr=account_rr&slot=3&rec=mt')
driver.get('https://app.psw.gov.pk/app/Dashboard')
sleep(10)
