from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = 'C:\Program Files (x86)\Python37-32\chromedriver.exe'

b = webdriver.Chrome(path)
b.get('http://wap.skylongtech.com/wap/dist/#/AppIndex')
time.sleep(2)
b.set_window_size('414','736')

confirm = b.find_element_by_class_name('btn')
time.sleep(1)
confirm.click()

signin = b.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/a')
time.sleep(1)
signin.click()

UserID = b.find_elements_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/input')
UserID.send_keys('joeuse1010')

PSW = b.find_elements_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/input')
PSW.send_keys('a123456')

