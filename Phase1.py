#Imported Libraries
import imp
from msilib.schema import Class
from bs4 import BeautifulSoup
import selenium
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class dnsdumpster:
    def __init__(self, domainname ):
        print("The domain you entered is [", domainname, "].")

    def initializeDriver(self, path):
        Path = path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get("https://dnsdumpster.com")
        return driver
    def searchDomain(self, domainName, driver):
        print(domainName)
        search = driver.find_element(By.CLASS_NAME, "form-control")
        search.send_keys(domainName)
        search.send_keys(Keys.RETURN)
    def initalizeSoup(self):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    def subdomainList(self, soupvar):
        subdomains = []
        p_tags = soup.select('div.table-responsive td[class="col-md-4"]')
        for ptags in p_tags:
            subdomains.append(ptags.get_text(strip=True))
        return subdomains
    def listToString(self, s):
        str1 = " " 
        return (str1.join(s))
    def regexFind(self, subdomains_str):
        r = re.findall("(([a-z0-9-]+\.)\.?([a-z0-9-]+\.)?((.[a-z0-9-]+\.)?([A-Za-z]+\.[a-z]+)))", subdomains_str)
        return r
    def createSubdomainFile(self):
        try:
            f = open("DDS.txt", "x")
        except:
            print("File already exists. Opening the current file and writing in it. ")
            f = open("DDS.txt", "w")
        return f
    def printStoreSubdomains(self, regexoutput, file):
        count = 0
        for finalSubdomain in regexoutput:
            print(finalSubdomain[0])
            file.write(finalSubdomain[0])
            file.write("\n")
            count = count + 1
        print("[-]", count,"subdomains were found !")
    


#-----------------------------------------------------


PATH = "C:\Program Files (x86)\chromedriver.exe"


DomainName = input("[-]Enter the Domain: ")
ob = dnsdumpster(DomainName)
driver = ob.initializeDriver(PATH)
ob.searchDomain(DomainName, driver)
try:
    subdomains = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
    )
    Dns_records = subdomains.find_element(By.CLASS_NAME, "table")
except:
    print("[!]Error !!. Check the entered domain once again.")
    driver.quit()

soup = ob.initalizeSoup()
Subdomains = ob.subdomainList(soup)
subString = ob.listToString(Subdomains)
regexOut = ob.regexFind(subString)
fileVar = ob.createSubdomainFile()
ob.printStoreSubdomains(regexOut, fileVar)
