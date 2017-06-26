from json import loads
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import re
import time
#url = "http://www.xn--knhit-hsa.vn/2017/04/tong-hop-cac-khoa-hoc-tren-udemy-mien-phi-cap-nhat-hang-ngay.html"
url = "https://enqtran.com/khoa-hoc-udemy-mien-phi-hang-ngay/"
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
#links = re.findall('"((http)s?://.*?)"', html)
links = re.findall('https:\/\/www.udemy.com\/\S+', html)
print (links)
chromedriver ='C://Users//phong//Documents//chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.udemy.com/join/login-popup/")
time.sleep(5)
username = driver.find_element_by_id("id_email")
username.send_keys("username")
password = driver.find_element_by_id("id_password")
password.send_keys("pass")
time.sleep(2)
driver.find_element_by_id("submit-id-submit").click()
#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
for a in links:
    driver.get(a)
    time.sleep(2)
    link = driver.find_element_by_link_text('Enroll Now')
    link.click()





