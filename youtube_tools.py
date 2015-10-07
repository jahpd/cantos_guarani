from urllib2 import urlopen
from bs4 import *
import re
import datetime
from iso88591 import *

def soup_url(url):   
    print "=> %s: requesting %s " % (datetime.datetime.now(), url)
    html = urlopen(url).read()
    return  BeautifulSoup(html, "lxml")

def soup_string(html):
    return BeautifulSoup(html, "lxml")

def get_videos(soup):
    items = soup.find('ol', id=re.compile(r'item-section-[0-9]*'))
    for item in items.find_all('li'):
        # titulo
        t = item.find('a', title=re.compile(r'\w*'))
        
        if t != None:
            d = {"url": t['href'], "title": t['title']}

            # metainfo
            url = "https://www.youtube.com%s" % d["url"]
            _bs = soup_url(url)
            d["description"] = {}
            d["description"]["info"] = _bs.find('div', id="watch-uploader-info").text
            d["description"]["text"] = _bs.find('p', id="eow-description").text
            write_data(d)
            
    
    link= "https://www.youtube.com%s" % soup.find('div', class_="yt-uix-pager search-pager branded-page-box spf-link ").find('a', {"data-link-type": "next", "href": re.compile(r'\/results\?search_query=[a-zA-Z0-9]+(\+[a-zA-Z0-9]+)*\&page=[0-9]+')})['href']

    if link:
        get_videos(soup_url(link))

    
def write_data(item):
    path = "./data/%s.txt" % item["url"].split("/watch?v=")[1]
    print "Writing %s" % path
    f = open(path, "w")
    f.write("%s\n\n" % encode_utf8_to_iso88591(item["title"]))
    f.write("%s\n\n" % encode_utf8_to_iso88591(item["description"]["info"]))
    f.write("%s\n\n" % encode_utf8_to_iso88591(item["description"]["text"]))
    f.close()
