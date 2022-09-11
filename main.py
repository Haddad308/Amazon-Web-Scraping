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
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7"} 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(Path,options=options)


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
        Data['about_item'].append(soup.find("div",{"id":"feature-bullets"}).text)
        Data['tech_info'].append(soup.find("table",{"id":"productDetails_techSpec_section_1"}).text)
        Data['additional_info'] .append(soup.find("table",{"id":"productDetails_detailBullets_sections1"}).text)
        print(f"product scrapped Succefully")
    except :
        Data['title'].append(np.nan)
        Data['price'].append(np.nan)
        Data['product_image'].append(np.nan)
        Data['specs'].append(np.nan)
        Data['about_item'].append(np.nan)
        Data['tech_info'].append(np.nan)
        Data['additional_info'] .append(np.nan)
        print("Error while scraping")



def get_reviews(URL):
    try : 
        driver.get(URL)
        get_review  = driver.find_element(By.XPATH,'//*[@id="reviews-medley-footer"]/div[2]/a')
        get_review.send_keys(Keys.RETURN)
        url_ =  driver.current_url
        page = requests.get(url_, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        Data['reviews'].append(soup.find("div",{"id":"cm_cr-review_list"}).text.strip())
    except : 
        Data['reviews'].append("No reviews Founded")



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
    page_products_links = soup.find_all('a',{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    for url_structure in page_products_links:
        counter += 1 
        half_url = url_structure.attrs['href']
        url = f"https://www.amazon.eg/{half_url}"   
        print(f"{counter}-",end="") 
        get_information(url)
        get_reviews(url)
        time.sleep(1)
        
    
    
    print(f"Page ({iter}) Scrapped Successfully")
    # Scraping 3 pages only 
    test += 1 
    if (test == 3):
        break 




# Saving_Data
dataframe = pd.DataFrame(Data)
dataframe.to_csv("Desktop/Amazon.csv" , index=False , encoding="utf-8" )


# Say Good bye 
driver.close()