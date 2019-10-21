import csv
from scraper import get_product_details
from url_response import get_custom_url


def read_csv():
    with open('ScrapperSheet2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        man_part_nums = []
        for row in csv_reader:
            man_part_nums.append(row[1])
        set_part_nums = set(man_part_nums)
        i_s_part_nums = iter(set_part_nums)
        # next(i_s_part_nums)
        print("\n")
        for part_num in i_s_part_nums:
            # get_product_details(part_num)
            product_url = get_custom_url(part_num)
            print(product_url)
            product_info = get_product_details(product_url, part_num)
            if (product_info == "None"):
                print("No Products Found")
            else: 
                print(product_info)
            

# # function call
read_csv()













#----------------------------------------------------------------------------------------------------------------------------------------#
# productFile = open('scrappersheet2.csv')
#     productReader = csv.reader(productFile)
#     # productData = list(productReader)
#     for partNum in productReader[][2]:
#         print(str(partNum)) #prints second column: part number
