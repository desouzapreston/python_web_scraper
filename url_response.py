from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import urlretrieve
from urllib.request import urlopen


def get_custom_url(part_num):
    dict_url = {'p': part_num}
    pstr = urlencode(dict_url)
    custom_str = urlretrieve("https://www.newegg.com/p/pl?" + pstr)
    print(custom_str)
    return custom_str
    
#function call
get_custom_url("006515-OM2-PAK")
    
    
    
    
    
    # #----------BEAUTIFUL SOUP----------#
    # # creating beautiful soup object
    # response = urlopen("https://www.newegg.com/p/pl?d=Voyager+Pro+Carry+Case")
    # html = response.read()
    # # print(html)
    # soup = BeautifulSoup(html.decode("utf-8"), "html.parser")