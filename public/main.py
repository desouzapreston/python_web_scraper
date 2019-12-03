import sqlite3

#db
conn = sqlite3.connect('new_egg.db')
cur = conn.cursor()
# cur.execute('CREATE TABLE scrapings (title VARCHAR, price VARCHAR, image VARCHAR)')
# conn.commit()

def main(conn, cur):
    #Get title, price, img_thumbnail_url, 
    i_s_parts_nums = read_csv()
    for part_num in i_s_part_nums:
        product_url = get_custom_url(part_num)
        print(product_url)
        product_info = get_product_details(product_url, part_num, cur, conn)
        print(product_info)
        print("\n")
            


# function call
main(conn, cur)

#DB End Connection        
conn.close()