# python package
import csv
import time
import random
import sys
import subprocess

# subprocess package
from subprocess import Popen

# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException

# configurer webdriver
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver1 = webdriver.Chrome(executable_path='./drivers/chromedriver')
wait = WebDriverWait(driver, 20)
wait1 = WebDriverWait(driver1, 20)

# modele
modele = ( sys.argv[2] )

# aller sur la page d accueil
base_url = ( sys.argv[1] )
driver.get(base_url)

wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='rgpd-btn-index-accept']"))
            )

Cookies = driver.find_element_by_xpath("//*[@id='rgpd-btn-index-accept']")
Cookies.click()

# attendre le chargement
try:
    wait.until(EC.element_to_be_clickable(
                    (By.ID, "listing-infinite"))
                )
except (TimeoutException):
    sys.exit("Error message - loading page")

indispo = "DISPONIBLE"
indispo = str(indispo)

# ouvrir csv
with open('dispo.csv', 'w') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # ouvrir toutes les pages produits
    products = driver.find_elements_by_css_selector('article')
    i = 0

    for product in products:
        url_product = product.find_element_by_css_selector("a").get_attribute('href')
        i = i + 1

        # disponibilite
        try:
            prix = product.find_element_by_css_selector("span[class^='item__price']").text.encode('utf-8')
            prix = str(prix)      

        except(NoSuchElementException):
            product_availability = "0"

        if indispo in prix:
            product_availability = "0"
        else:
            product_availability = "1"

        
        if product_availability == "1":
            
            driver1.get(url_product)
            wait1.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rgpd-btn-index-accept']")))
            driver1.find_element_by_xpath("//*[@id='rgpd-btn-index-accept']").click()
            try:
                product_price = driver1.find_element_by_css_selector("span[class^='dyn_prod_price']").text.encode('utf-8')
                subprocess.Popen( ["python", "achatrdc.py", url_product, modele, product_price])
            except(NoSuchElementException):
                pass
        else: 
            pass

# fermer les navigateurs
driver.close()
driver1.close()