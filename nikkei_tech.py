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
outputfile = open('nikkei_tech_tech.txt','w')
for line in filename:
    if re.search(r'http*',line):
        line = line.rstrip()
        http_text = line.split(' ')
        if re.search(r'http*',line):
            if is_japanese(line) == False:
                url = line.lstrip()
                try:
                    fp=urlopen(url)
                except urllib.error.HTTPError as e:
                    pass
                except urllib.error.URLError as e:
                    pass
                soup = BeautifulSoup(fp.read(), "html.parser")

                print('---------------',file=outputfile)
                if soup.title != None:
                    print(soup.title.string,file=outputfile)

                texts = soup.find("div",class_="abstract")
                if texts == None:
                    texts = soup.find(id="kiji")
                elif texts == None:
                    texts = soup.find(class_="article-body")
                elif texts == None:
                    texts = soup.find(id="contents")

                if texts == None:
                    print(url,file=outputfile)

                print(texts,file=outputfile)

                #for word in texts:
                    #print(word.string,file=outputfile)
