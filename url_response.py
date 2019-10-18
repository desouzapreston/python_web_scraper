from bs4 import BeautifulSoup
from urllib.parse import urlencode, quote, unquote, urlparse
from urllib.request import urlretrieve
from urllib.request import urlopen


def get_custom_url(part_num):
    url = "https://www.newegg.com/p/pl?d=%s" % (part_num)
    print(url)

#function call
get_custom_url("81293-01")
    
    
    
    
    
    # #----------BEAUTIFUL SOUP----------#
    # # creating beautiful soup object
    # response = urlopen("https://www.newegg.com/p/pl?d=Voyager+Pro+Carry+Case")
    # html = response.read()
    # # print(html)
    # soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    
    # pstr = quote(part_num)
    # # dict_url = {'p': part_num}
    # # pstr = urlencode(dict_url)
    # custom_str = urlretrieve("https://www.newegg.com/p/pl?" + pstr)
    # parsed_custom_str = urlparse(custom_str)
    # print(unquote(parsed_custom_str))
    # return custom_str
    