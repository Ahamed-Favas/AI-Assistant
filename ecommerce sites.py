from os import link
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

choice = input("Enter the  ecommerce sites (amazon,flipkart):")
if choice=="amazon":
    product=input("Enter the product you want to buy:")
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\91623\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    sleep(2)
    txtproduct=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    txtproduct.send_keys(product)
    sleep(2)
    login_box = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
    sleep(2)
    login_box.submit()
    while True:
        pass

else:

    product=input("Enter the product you want to buy:")
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\91623\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.flipkart.com/')
    driver.maximize_window()
    sleep(2)
    link = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
    link.click()
    sleep(2)
    txtproduct=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    txtproduct.send_keys(product)
    txtproduct.send_keys(Keys.ENTER)
    sleep(4)
    
    while True:
        pass