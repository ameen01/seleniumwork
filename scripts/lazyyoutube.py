from selenium import webdriver
import time
import random


bset_music = ['j cole', '50 cent', 'kendrick lamar', 'roy woods', 'wiz khalifa', 'sammie', ]

ons_video = random.choice(bset_music)

locking_for = ons_video

youtube = webdriver.Firefox(executable_path='./geckodriver')
youtube.get('https://www.youtube.com/')
time.sleep(1)
search = youtube.find_element_by_name('search_query')
click_btn = youtube.find_element_by_id('search-icon-legacy')

text = search.send_keys(locking_for)
click = click_btn.click()
time.sleep(2)
video = youtube.find_element_by_id('thumbnail')
time.sleep(3)
c = video.click()
