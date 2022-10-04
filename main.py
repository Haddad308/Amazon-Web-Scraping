from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np 
import requests 
import time

# Information of Setup 
Path = "C:\\Program Files (x86)\\chromedriver.exe"
#         ...... To see full code call +201281982770 whatsapp

## Data Container
Data = {'title':[],
        'price':[],
        'product_image':[],
        'specs':[],
        'about_item':[],
        'tech_info':[],
        'additional_info':[],
        'reviews':[]
        }

def get_information(URL):
    try :
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        Data['title'].append(soup.find("span",{"id":"productTitle"}).text.strip())
        Data['price'].append(soup.find("span",{"class":"a-price-whole"}).text.split()[0])
        Data['product_image'].append(soup.find("img",{"id":"landingImage"}).attrs['src'])
        Data['specs'].append(soup.find("div",{"id":"poExpander"}).text)
#         ...... To see full code call +201281982770 whatsapp 


def get_reviews(URL):
    try : 
        driver.get(URL)
        get_review  = driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a')
#         ...... To see full code call +201281982770 whatsapp


# Start point 
MAIN_URL = "https://www.amazon.eg/s?i=electronics&rh=n%3A21832907031&fs=true&page=1&language=en&qid=1660139874&ref=sr_pg_2"
driver.get(MAIN_URL)

# Pages counter 
test = 0 

# All Pages Scrapping 
page = requests.get(MAIN_URL, headers=headers)
soup = BeautifulSoup(page.content,'lxml')



# Calculate Number of pages we are going to scrap 
Number_of_products = int(soup.find('div',{"class":"a-section a-spacing-small a-spacing-top-small"}).text.split()[2])
Number_of_products_per_page = int(soup.find('div',{"class":"a-section a-spacing-small a-spacing-top-small"}).text.split()[0].split("–")[1])
Number_of_pages = int(Number_of_products / Number_of_products_per_page)

counter = 0
for iter in range(1,Number_of_pages):
    MAIN_URL = f"https://www.amazon.eg/s?i=electronics&rh=n%3A21832907031&fs=true&page={iter}&language=en&qid=1660139874&ref=sr_pg_2"
#         ...... To see full code call +201281982770 whatsapp
        
    
  




# Saving_Data
dataframe = pd.DataFrame(Data)
dataframe.to_csv("Desktop/Amazon.csv" , index=False , encoding="utf-8" )


# Say Good bye 
driver.close()
