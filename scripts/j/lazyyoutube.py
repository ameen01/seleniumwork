from selenium import webdriver
import time

locking_for = '50 cent'

youtube = webdriver.Firefox(executable_path='./geckodriver')
youtube.get('https://www.youtube.com/')
time.sleep(1)
search = youtube.find_element_by_name('search_query')
click_btn = youtube.find_element_by_id('search-icon-legacy')

text = search.send_keys(locking_for)
click = click_btn.click()
time.sleep(3)
video = youtube.find_element_by_id('thumbnail')

c = video.click()