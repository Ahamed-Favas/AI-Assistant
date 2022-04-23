from time import sleep
from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
username="sdsd"
password="hhgjhhjgjmhj"
# username=input("Enter Your Facebook username,email or phone no.:")
# passwd=getpass("Enter your Facebook password:")
#driver=webdriver.Chrome(ChromeDriverManager().install)
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