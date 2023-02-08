from selenium import webdriver
import time

"""" script to whatch tv show in sdarot """

browser = webdriver.Firefox(executable_path="./geckodriver")

browser.get("https://sdarot.work")
time.sleep(1)

searsh = browser.find_element_by_id("liveSearch")
searsh.send_keys("Homeland")

time.sleep(2)
submit = browser.find_element_by_class_name("input-group-btn").click()

eposde = browser.find_element_by_xpath("/html/body/div/section[1]/div[2]/div/div[2]/ul[2]/li[1]").click()
time.sleep(33)
if browser.find_element_by_id("proceed"):
    browser.find_element_by_id("proceed").click()
    time.sleep(2)
    browser.find_element_by_class_name("vjs-big-play-button").click()
    browser.find_element_by_class_name("vjs-fullscreen-control vjs-control vjs-button").click()

