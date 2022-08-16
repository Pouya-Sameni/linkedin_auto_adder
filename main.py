# Import Library
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
from decouple import config


userFile = open(config("csvFile"), 'r')
# set webdriver path here it may vary
# Its the location where you have downloaded the ChromeDriver
driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")

# Get the target URL
driver.get('https://www.linkedin.com')



# Wait for 5 seconds to load the webpage completely
#time.sleep(5)
login = driver.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/button')
user = driver.find_element('xpath', '//*[@id="session_key"]')
password = driver.find_element('xpath', '//*[@id="session_password"]')


user.send_keys(config("user"))
password.send_keys(config("pass"))
login.click()


#time.sleep(5)

for line in userFile:
    try:
        driver.get(line)
        time.sleep(5)

        connectButton2 = driver.find_element('xpath', '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button')
        buttonText2 = str(connectButton2.text)
        time.sleep(5)


        if buttonText2.lower() == 'connect':
            print("Working on " + line)
            connectButton2.click()
            time.sleep(5)
            sendButton = driver.find_element('xpath', '/html/body/div[3]/div/div/div[3]/button[2]')
            sendButton.click()
            time.sleep(5)

       
    except:
        print ("Skpping.." + line)


driver.close()