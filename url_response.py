from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlencode, quote, unquote, urlparse
from urllib.request import urlretrieve
from urllib.request import urlopen


def get_custom_url(part_num):
    args = {"d": part_num}
    url = "https://www.newegg.com/p/pl?{}".format(urllib.parse.urlencode(args))
    # print(url)
    return url
