from time import sleep
from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

choice = input("Enter the social media (facebook,instagram):")
if choice=="facebook":
    username=input("Enter Your Facebook username,email or phone no.:")
    password=getpass("Enter your Facebook password:")
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\91623\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.facebook.com/')
    driver.maximize_window()
    sleep(2)
    txtUsername=driver.find_element_by_id('email')
    txtUsername.send_keys(username)
    txtpasswd=driver.find_element_by_id('pass')
    txtpasswd.send_keys(password)
    sleep(2)
    login_box = driver.find_element_by_css_selector("button[name='login']")
    sleep(2)
    login_box.submit()
    while True:
        pass

else:

    username="sdsd"
    password="hhgjhhjgjmhj"
    username=input("Enter Your instagram username,email or phone no.:")
    passwd=getpass("Enter your instagram  password:")
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\91623\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.instagram.com/?hl=en')
    driver.maximize_window()
    sleep(2)
    txtUsername=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    txtUsername.send_keys(username)
    txtpasswd=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    txtpasswd.send_keys(password)
    sleep(2)
    login_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    login_box.submit()
    while True:
        pass