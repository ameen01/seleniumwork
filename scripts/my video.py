from selenium import webdriver
import time

cont = 0
while cont < 20:
    youtube = webdriver.Firefox(executable_path='./geckodriver')
    youtube.get('https://www.youtube.com/watch?v=JwZJaBKirDI')
    clic = youtube.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()
    time.sleep(30)
    youtube.get('https://www.youtube.com/watch?v=0UI96RCvq2Y')
    time.sleep(2)
    click = youtube.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()
    time.sleep(50)
    cont += 1
