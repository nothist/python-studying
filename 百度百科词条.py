from urllib.request import urlopen
from urllib.error import HTTPError
import re
from bs4 import BeautifulSoup as bts

try:
    html = urlopen("https://baike.baidu.com/item/gooogle")
except HTTPError as e:
    print(e)
else:
    if html is None:
        print('None')
    else:
        bsobj = bts(html.read(), "html.parser")
        title = bsobj.h1.get_text()
        dtlist = bsobj.findAll("dt", {"class": "basicInfo-item name"})
        ddlist = bsobj.findAll("dd", {"class": "basicInfo-item value"})

        print(title + ':')
        for name, value in zip(dtlist, ddlist):
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            name = re.sub(pattern, '', str(name))
            print('\t' + name + ' : ' + value.get_text().strip())
