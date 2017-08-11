#!/usr/bin/env python

import sys
import json
import re
from newspaper import Article


def Pars(url):
 
    article = Article(url, language='ru')
    article.download()

    try:
        article.parse()
    except:
        return ''
    
    text = article.text
    text = ' '.join(text.split())

    return (text)


for url in sys.stdin:
    try:
        text = Pars(url.replace('\n', ''))
    except:
        text = ''
 
    try:    
        print (str(url)+'\t'+text).encode('utf-8')
    except:
        try:
            print (str(url)+'\t'+text).encode('utf-8').decode('utf-8')
        except:
            try:
                print (str(url)+'\t'+text).decode('utf-8')
            except:
                print ('')
