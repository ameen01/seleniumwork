from selenium import webdriver
import time

exe = webdriver.Firefox(executable_path='./geckodriver')
searcj = exe.get('https://www.google.com/')

google = exe.find_element_by_name('q')
google.send_keys("kiz")

time.sleep(2)
exe.find_element_by_name("btnK").click()
time.sleep(1)
o = exe.find_elements_by_tag_name('a')
s= o[0]
s.click()
print(s)

# exe.back()
# exe.close()