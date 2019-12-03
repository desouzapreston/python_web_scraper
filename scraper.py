from urllib import request, response, error, parse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


def get_product_details(custom_url, part_num, cur, conn):
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
            price_dollar = price_current.find("strong").get_text()
            price_cent = price_current.find("sup").get_text()
            price = price_dollar + price_cent
            product_info["Price: "] = price
            #Image:
            item_image = item_container.find("a", class_="item-img")
            image_full = item_image.find("img")
            image = image_full['src']
            product_info["Img: "] = image
            cur.execute("INSERT OR IGNORE INTO scrapings (title, price, image) VALUES (?, ?, ?)",
            (title, price, image))
            conn.commit()
        return product_info

