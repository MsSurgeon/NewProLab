#!/usr/bin/python

import sys
import re
import urlparse
import urllib

doms = {u'cars.ru', u'avto-russia.ru', u'bmwclub.ru', u'sp.krasmama.ru', u'forum.krasmama.ru', u'forum.omskmama.ru', u'novayagazeta.ru', u'echo.msk.ru', u'inosmi.ru'}

def url2domain(url):
   try:
       a = urlparse.urlparse(urllib.unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
   except:
       return

def do_map(row):
    word = row.strip().split('\t')
    try:
        if (word[0] != "-") and word[0].isdigit() and (word[2] != "-"):
            dom = url2domain(word[2])
            if (dom.strip() != '') and (dom in doms):
                yield word[0], dom
    except:
        return

for line in sys.stdin:
    for key, val in do_map(line):
        print(key + "\t" + val + "\t1")
