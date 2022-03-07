from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import time

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

url = 'https://marshemispheres.com/'
browser.visit(url)

image_dict=[]

for n in range(4):
    image_link = browser.find_by_tag('h3')[n]
    image_link.click()
    time.sleep(2)
    html = browser.html
    img_soup = soup(html, "html.parser")
    d_img = img_soup.find(class_='container')
    full_img=d_img.find_all('li')[0]
    full_img_url=full_img.find(href=True).get('href')
    title = img_soup.find(class_='title').getText()
    image_dict.append({'title': title, 'full_img':url+full_img_url})
    browser.back()        
print(image_dict)