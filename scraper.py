# from requests.models import PreparedRequest
from urllib import request, response, error, parse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import time  # local variable 'title' referenced before assignment
# import csv
# import sqlite3
# from reader import *


def get_product_details(custom_url, part_num):
    # finding item list section
    html = custom_url
    response = urlopen(custom_url)
    html = response.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    if not (soup.find_all("div", class_="result-message")):
        product_info = {}
        section = soup.find_all("div", class_="items-view")
        for item_container in section:
            #Title:
            item_info = item_container.find("div", class_="item-info")
            title = getattr(item_info.find("a", class_="item-title"), "string", "none")
            product_info["Title: "] = title

            #Price:
            item_action = item_info.find("div", class_="item-action")
            price_section = item_action.find("ul", class_="price")
            price_current = price_section.find("li", class_="price-current")
            # print(price_current)
            price_dollar = price_current.find("strong").get_text()
            price_cent = price_current.find("sup").get_text()
            price = price_dollar + price_cent
            product_info["Price: "] = price

            # price_current_label = getattr(price_current.find("span", class_="price-current-label"), "string", "none")
            # price_current_label = price_current.find("span", "price-current-label").text

            #Image:
            item_image = item_container.find("a", class_="item-img")
            image_full = item_image.find("img")
            image = image_full['src']
            product_info["Img: "] = image


        time.sleep(.1)
        return product_info

#----------------------------------------------------------------------------------------------------------------------------------------#
# try:
# except AttributeError:            
# title = "Title: -"
# except UnboundLocalError:
#     title = "Title: -"
# try:

# def getTitle(soup):
#     section = soup.find_all("div", class_="items-view")
#     for item_container in section:
#         item_info = item_container.find("div", class_="item-info")
#         title_line = item_info.find("a", class_="item-title")
#         # print(title_line)
#         try:
#             time.sleep(.1)
#             title = title_line.get_text()
#         except AttributeError:
#             title = "Title: -"
#         except UnboundLocalError:
#             print("No Product Data Found")
#     time.sleep(.1)
#     return title
# function call

# getProductDetails()


# section = soup.find_all(‘section’, class_=’page-section’)
# for elem in section:
#     inner = elem.find_all(‘div’)
#     for has_side in inner:
#         inner = has_side.find_all(‘div’)
#         for row_body in inner:
#             inner = row_body.find_all(‘div’)
#             for row_body_inner in inner:
#                 inner = row_body_inner.find_all(‘div’)
#                 for row_body_border in inner:
#                     inner = row_body_border.find_all(‘div’)
#                     for

# #sqlite connection
# conn = sqlite3.connect("\sqlite3\sqlite-tools\db\newegg.db")
# cur = conn.cursor()

# # csv data
# with open('ScrapperSheet2.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(f'\t{row[0]}, {row[1]}, {row[2]}')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

# #pushing to sqlite.db file newegg.db
# for item in collected_items:
#     cur.execute("INSERT INTO scraped_data (title, price, url) values (?, ?, ?)",
#                 (item["title"], item["price"], item["url"])
#                 )

#----------Checks and status codes----------#
# print(r.status_code)
# #Status code 200 Ok
# print(req.headers.get("content-type", "unknown"))
# #text/html; charset=utf-8

# # beautiful soup parser
# soup = BeautifulSoup(req.text, "html.parser")
# for product in soup.find_all("div", "products"):
#     product_title = product.find("h3").text
#     product_price = product.find("span", "price").text
#     product_url = product.find("a")["href"]
#     print("{} is selling for {} at {}".format(
#         product_title, product_price, product_url))

# #preparing our URL
# req = PreparedRequest()
# url = "https://www.newegg.com/p/pl"
# params = {'d':"EWS7926EFP"}
# req.prepare_url(url, params)
# print(req.url)
