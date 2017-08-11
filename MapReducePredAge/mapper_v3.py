#!/usr/bin/env python

import sys
import json
import re
from urlparse import urlparse
from urllib import urlretrieve, unquote, urlopen
import xml.etree.cElementTree as ET
import requests
import nltk
import bs4

def ParseHTML_v2(url):
    text = ''
    try:
        html = urlopen(url).read()
        soup = bs4.BeautifulSoup(html)
        [s.extract() for s in soup(['style', 'script', '[document]', 'head'])]
        text = ' '.join(soup.getText().split())
    except:
        pass
    return text

def get_url(url):
    try:
        a = urlparse(unquote(url.strip()))
        if a.netloc == 'news.yandex.ru':
                if(re.search('(?<=cl4url=).+(html)', url)):
                    url = 'http://' + re.search('(?<=cl4url=).+(html)', url).group(0)
                else:
                    url = 'http://' + re.search('(?<=cl4url=).+', url).group(0)
        stripUrl = str(url).strip()
        return stripUrl
    except:
        return url

user_text = ''

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) < 4:
        continue
        
    j = json.loads(parts[3])
    for visit in j['visits']:
        url = get_url(visit['url'].encode('utf-8'))
        ts = visit['timestamp']
        
        try:
            text  = ParseHTML_v2(url)
            user_text = user_text + ' ' + text
        except:
            continue
    
    try:
        print (parts[0]+'\t'+parts[1]+'\t'+parts[2]+'\t'+user_text).encode('utf-8').decode('utf-8')        
        #print '#######1######'
    except:
        try:
            print (parts[0]+'\t'+parts[1]+'\t'+parts[2]+'\t'+user_text).decode('utf-8')
            #print '#######2######'
        except:
            try:
                print (parts[0]+'\t'+parts[1]+'\t'+parts[2]+'\t'+user_text.encode('utf-8'))
                #print '#######3######'
            except:
                try:
                    print (parts[0]+'\t'+parts[1]+'\t'+parts[2]+'\t'+user_text.encode('utf-8').decode('utf-8'))
                    #print '#######4######'
                except:
                    print (parts[0]+'\t'+parts[1]+'\t'+parts[2]+'\t'+'None')
                    #print '#######5######'
