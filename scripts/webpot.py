from selenium import webdriver
import time

""" this script will log you in to facebook automatic
    all you need to do is to write your email/phone and password
"""
email_phone = 'huack@you.know'
password = '4fun'

browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get('https://www.facebook.com/')
time.sleep(1)

# find the filed in the html
email_location = browser.find_element_by_id('email')
password_location = browser.find_element_by_id('pass')

# write your email into the html filed
email_location.send_keys(email_phone)

# write your password into the html filed
password_location.send_keys(password)
time.sleep(2)
sing_in = browser.find_element_by_id('loginbutton').click()
print(browser)


