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
        print("\n")
        return i_s_part_nums

