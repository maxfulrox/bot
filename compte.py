from selenium import webdriver
import time

web = webdriver.Chrome(executable_path='./drivers/chromedriver')
web.get('https://secure2.ldlc.com/fr-fr/Login/Register')

time.sleep(2)

Cookies = web.find_element_by_xpath('//*[@id="cookieConsentAcceptButton"]')
Cookies.click()

time.sleep(2)

Mail = "max@gmail.com"
last = web.find_element_by_xpath('//*[@id="Email"]')
last.send_keys(Mail)

time.sleep(2)

Mdp = "123-Test"
last = web.find_element_by_xpath('//*[@id="Password"]')
last.send_keys(Mdp)

time.sleep(2)

Sexe = web.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div[5]/div[2]/label')
Sexe.click()

time.sleep(2)

Prenom = "prenom"
last = web.find_element_by_xpath('//*[@id="FirstName"]')
last.send_keys(Prenom)

time.sleep(2)

Nom = "nom"
last = web.find_element_by_xpath('//*[@id="LastName"]')
last.send_keys(Nom)

time.sleep(2)

Valide = web.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/button')
Valide.click()
