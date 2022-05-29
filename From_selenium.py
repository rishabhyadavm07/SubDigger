# TASK = Automate and then scrap the subdomains returned
# by dnsdumpster and save them to a file (well organised and ready to be supplied to the next program)

#1st tut

from cgitb import text
from unicodedata import name
from xml.dom.minidom import Element
from pyparsing import Dict

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from bs4 import BeautifulSoup


PATH = "C:\Program Files (x86)\chromedriver.exe"

#Error handling 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#DONE


# driver = webdriver.Chrome(executable_path = PATH)
# Driver setted up successfully 
driver.get("https://dnsdumpster.com")
print(driver.title)# prints the title of the webpage 
# driver.close()#closes only the tab that is opened
# driver.quit()#closes the whole chrome program 



#2nd tut

# methodology of serching a Element
# 1/ id
# 2/ name
# 3/ class
# 4/ etc

#<input class="form-control" type="text" placeholder="exampledomain.com" name="targetip" id="regularInput" autofocus="">

search = driver.find_element(By.CLASS_NAME, "form-control")
search.send_keys("google.com")
search.send_keys(Keys.RETURN)
# time.sleep(5)   

#class="col-md-4"
# subdomains1 = search.find_element_by_class_name("col-md-4")
# print(search.text)
#---------------------------------------------------------


try:
    subdomains = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
    )
    # print(subdomains.page_source)
    Dns_records = subdomains.find_element(By.CLASS_NAME, "table")
    # print(Dns_records.text)
except:
    driver.quit()
# print(driver.page_source)#wacks out the source code of the web page
# driver.close()
#----------------------------------------------------------
#Embedding beautifulSoup

html = driver.page_source

print(type(html))
# print(html)
soup = BeautifulSoup(html, 'lxml')

# col_md_3 = BeautifulSoup(html)

Total_subdomains = 0

main_tag = soup.find_all( class_ ='col-md-4')

main_tag_ip = soup.find_all('td' , {'class' :'col-md-3'})


for tag_ip in main_tag_ip:
    print(tag_ip.text)