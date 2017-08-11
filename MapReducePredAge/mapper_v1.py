#!/usr/bin/env python

import sys
import json
import re
from urlparse import urlparse
from newspaper import Article
import nltk

def ParseHTML_v1(article):
    text = date = ''
    try:
        article.download()
        article.parse()
        text = article.text
    except:
        html = article.html.encode('utf-8')
        text = re.sub(r'\s+', ' ', nltk.clean_html(html))
    return text

for line in sys.stdin:
    try:
	gender, age, uid, user_json = line.strip().split('\t')
    except ValueError:
	#logging.warn("Could not split line: %s", line)
	continue
	
    visits = json.loads(user_json)
    user_text = ''
    for visit in visits.get('visits'):
        url = visit['url'].encode('utf-8')
        ts = visit['timestamp']
        parsed_uri = urlparse(url)
        netlog = '{uri.netloc}'.format(uri=parsed_uri)
        try:
            path = '{uri.path}'.format(uri=parsed_uri)
        except:
            path = url
        if netlog == 'news.yandex.ru':
            if(re.search('(?<=cl4url=).+(html)', url)):
                ya_url = 'http://' + re.search('(?<=cl4url=).+(html)', url).group(0)
                article = Article(ya_url, language='ru')
            else:
                try:
                    ya_url = 'http://' + re.search('(?<=cl4url=).+', url).group(0)
                    article = Article(ya_url, language='ru')
                except:
                    pass
            text = ParseHTML_v1(article)
        else:
            article = Article(url, language='ru')
            text  = ParseHTML_v1(article)
            
            text = ' '.join(text.split())
            try:
                user_text = user_text + ' ' + text
            except:
                try:
                    user_text = user_text + ' ' + text.decode('utf-8')
                except:
                    pass
        
    try:
        print (uid+'\t'+gender+'\t'+age+'\t'+user_text).encode('utf-8').decode('utf-8')        
        #print '#######1######'
    except:
        try:
            print (uid+'\t'+gender+'\t'+age+'\t'+user_text).decode('utf-8')
            #print '#######2######'
        except:
            try:
                print (uid+'\t'+gender+'\t'+age+'\t'+user_text.encode('utf-8'))
                #print '#######3######'
            except:
                try:
                    print (uid+'\t'+gender+'\t'+age+'\t'+user_text.encode('utf-8').decode('utf-8'))
                    #print '#######4######'
                except:
                    print (uid+'\t'+gender+'\t'+age+'\t'+'None')
                    #print '#######5######'
