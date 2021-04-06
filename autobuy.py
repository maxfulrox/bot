from selenium import webdriver
import time

web = webdriver.Chrome(executable_path='./drivers/chromedriver')
web.get('https://www.ldlc.com/fiche/PB00370065.html?offerId=AR202009070050')

time.sleep(2)

Cookies = web.find_element_by_xpath('//*[@id="cookieConsentAcceptButton"]')
Cookies.click()

time.sleep(2)

Panier = web.find_element_by_xpath('//*[@id="product-page-price"]/div[2]/a[1]')
Panier.click()

time.sleep(2)

Voir = web.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]')
Voir.click()

time.sleep(2)

PasserCom = web.find_element_by_xpath('//*[@id="form2"]/button')
PasserCom.click()

time.sleep(2)

NoGarantie = web.find_element_by_xpath('//*[@id="modal-pack-selection"]/div/div[2]/div[4]/div/div[2]/a')
NoGarantie.click()
