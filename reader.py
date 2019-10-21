import csv
from scraper import get_product_details
from url_response import get_custom_url
import sqlite3

#db
conn = sqlite3.connect('new_egg.db')
cur = conn.cursor()
# cur.execute('CREATE TABLE scrapings (title VARCHAR, price VARCHAR, image VARCHAR)')
# conn.commit()

def read_csv(conn, cur):
    with open('ScrapperSheet2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        man_part_nums = []
        for row in csv_reader:
            man_part_nums.append(row[1])
        set_part_nums = set(man_part_nums)
        i_s_part_nums = iter(set_part_nums)
        print("\n")
        for part_num in i_s_part_nums:
            product_url = get_custom_url(part_num)
            print(product_url)
            product_info = get_product_details(product_url, part_num, cur, conn)
            print(product_info)
            print("\n")
            
# function call
read_csv(conn, cur)

#DB End Connection        
conn.close()
