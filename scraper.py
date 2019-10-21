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
    response = urlopen(custom_url)
    html = response.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    product_info_list = []
    product_info_list.append(getTitle(soup))


def getTitle(soup):
    section = soup.find_all("div", class_="items-view")
    for item_container in section:
        item_info = item_container.find("div", class_="item-info")
        title_line = item_info.find("a", class_="item-title")
        # print(title_line)
        try:
            title = title_line.get_text()
        except AttributeError:
            title = "Title: -"
        except UnboundLocalError:
            print("No Product Data Found")
        time.sleep(.1)
        return title


#----------------------------------------------------------------------------------------------------------------------------------------#
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
