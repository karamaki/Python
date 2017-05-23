from bs4 import BeautifulSoup
import urllib.request
import sys
import re
from urllib.parse   import quote
from urllib.request import urlopen
import unicodedata

# 釧路高専内ではプロキシ指定が必要
# --------------------------------
arg = sys.argv
proxy_support = urllib.request.ProxyHandler({'http':r'http://p130437:Karamaki1202@157.114.16.93:8080', 'https':r'http://p130437:Karamaki1202@157.114.16.93:8080'})
#opener = urllib.request.build_opener(proxy_support)
#urllib.request.install_opener(opener)
auth = urllib.request.HTTPBasicAuthHandler ()
opener = urllib.request.build_opener ( proxy_support , auth , urllib.request.HTTPHandler )
urllib.request.install_opener(opener)
#------------------------------------


def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

filename = open('日経テクノロジー のコピー.txt','r')
outputfile = open('nikkei_tech_t.txt','w')
for line in filename:
    if re.search(r'http*',line):
        line = line.rstrip()
        http_text = line.split(' ')
        if re.search(r'http*',line):
            if is_japanese(line) == False:
                url = line.lstrip()
                print(url)
                try:
                    fp=urlopen(url)
                except urllib.error.HTTPError as e:
                    pass
                except urllib.error.URLError as e:
                    pass
                soup = BeautifulSoup(fp.read(), "html.parser")
                texts = soup.findAll("div",class_="abstract")
                print('---------------',file=outputfile)
                if soup.title != None:
                    print(soup.title.string,file=outputfile)
                if texts == []:
                    texts = soup.findAll("div",id="kiji")
                elif texts == []:
                    texts = soup.findAll("div",class_="article-body")
                elif texts == []:
                    texts = soup.findAll("div",class_="p4 clearfix")
                for word in texts:
                    print(word.get_text(),file=outputfile)
