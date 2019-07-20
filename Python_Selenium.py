#!/usr/bin/env python
# coding: utf-8

# #### Install Depenency
# > pip install selenium
# 
# > pip install bs4
# 
#  - Download chromedriver from: http://chromedriver.chromium.org/downloads
# 


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C://chromedriver.exe")
try:
    driver.get('https://s1.demo.opensourcecms.com/wordpress/wp-login.php') #Target url
    driver.implicitly_wait(2)
    username = driver.find_element_by_name("log")     
    password = driver.find_element_by_name("pwd")     
    username.send_keys("opensourcecms")               #input argument  (user id)
    password.send_keys("opensourcecms")               #input argument  (user password)
    driver.find_element_by_id("wp-submit").click()    #submit request
except Exception as ex:
    driver.quit()
    print ("Error: request error! ", ex)

try:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
except Exception as ex:
    driver.quit()
    print ("Error: html DOM error! ", ex)

try:
    results = soup.find_all('div', {'class' : 'welcome-panel-content'})
    #print('Found:', len(results), ' records')
    description = ''
    welome_msg  = ''
    for result in results:
        welome_msg = result.find('h2').text
        description = result.find('p', {'class' : 'about-description'}).text
    if (welome_msg == 'Welcome to WordPress!' or 'Bienvenue sur WordPress !'):
        print (welome_msg)
        print (description)
    else:
        print ("Welcome message not getting")
    driver.implicitly_wait(2)
    driver.quit()
except Exception as ex:
    driver.quit()
    print ("Error: html elemnt error! ", ex)


