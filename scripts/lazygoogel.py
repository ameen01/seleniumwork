from selenium import webdriver
import time

searching_for = '153'

google = webdriver.Firefox(executable_path='./geckodriver')
google.get('https://www.google.es/')
time.sleep(2)
search_bar = google.find_element_by_name('q')
btn = google.find_element_by_name('btnK')

# type what you searching for
text = search_bar.send_keys(searching_for)
time.sleep(1)
search_btn = btn.click()
