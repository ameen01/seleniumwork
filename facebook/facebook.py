from selenium import webdriver
import time

# automate log in to facebook and get friends list #
#  to do !
# make facebook accont
# install selenium to user path 
# dwonload selenium driver
#  
# get facebbok log in form
# ##
with open('usr','rt') as f:
    usrinfo = f.readlines()
    email = usrinfo[0]
    password = usrinfo[1]
    



url = 'https://www.facebook.com'

driver = webdriver.Firefox()




#log in usr
def log_in(email, password):
    email_filed = driver.find_element_by_id('email')
    email_filed.send_keys(email)
    time.sleep(1)
    passwrod_filed = driver.find_element_by_id('pass')
    passwrod_filed.send_keys(password)
    time.sleep(1)
    btn = driver.find_element_by_name('login').click()


#frinds list
def friends_list():
    profile = driver.find_element_by_css_selector('.x1us19tq > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
    profile.click()
    time.sleep(1)
    my_frinds = driver.find_element_by_css_selector('.x879a55 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4) > div:nth-child(1) > span:nth-child(1)').click()

driver.get(url)
time.sleep(2)

log_in(email,password)
time.sleep(2)
friends_list()


