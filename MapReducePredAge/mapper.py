#!/usr/bin/env python

import sys
import json
import re
from urlparse import urlparse
from newspaper import Article
import nltk

def ParseHTML(article):
    text = summary = date = ''
    authors = key_words = []
    try:
        article.parse()
        text = article.text
        authors = article.authors
        date = article.publish_date
        article.nlp()
        key_words = article.keywords
        summary = article.summary
    except:
        html = article.html.encode('utf-8')
        text = re.sub(r'\s+', ' ', nltk.clean_html(html))
    return text, authors, date, key_words, summary

for line in sys.stdin:
	try:
	   gender, age, uid, user_json = line.strip().split('\t')
	except ValueError:
		#logging.warn("Could not split line: %s", line)
		continue
	
	visits = json.loads(user_json)
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
                ya_url = 'http://' + re.search('(?<=cl4url=).+', url).group(0)
                article = Article(ya_url, language='ru')	
	    text, authors, date, key_words, summary = ParseHTML(article)
        else:
            article = Article(url, language='ru')
            article.download()
            text, authors, date, key_words, summary = ParseHTML(article)
        
        text = ' '.join(text.split())
        summary = ' '.join(summary.split())

        try:
            print (str(ts)+'\t'+url+'\t'+netlog+'\t'+path+'\t'+text+'\t'+str(date)+'\t'+str(list(authors))+'\t'+str(list(key_words))+'\t'+summary).encode('utf-8').decode('utf-8')        
            #print '#######1######'
        except:
            try:
                print (str(ts)+'\t'+url+'\t'+netlog+'\t'+path+'\t'+text+'\t'+str(date)+'\t'+str(list(authors))+'\t'+str(list(key_words))+'\t'+summary).decode('utf-8')
                #print '#######2######'
            except:
                try:
                    print (str(ts)+'\t'+url+'\t'+netlog+'\t'+path+'\t'+text.encode('utf-8')+'\t'+str(date)+'\t'+str(list(authors))+'\t'+str(list(key_words))+'\t'+summary.encode('utf-8'))
                    #print '#######3######'
                except:
                    try:
                        print (str(ts)+'\t'+url+'\t'+netlog+'\t'+path+'\t'+'None'+'\t'+str(date)+'\t'+str(list(authors))+'\t'+str(list(key_words))+'\t'+'None')
                        #print '#######4######'
                    except:
                        print (str(ts)+'\t'+url+'\t'+netlog+'\t'+path+'\t'+'None'+'\t'+str(date)+'\t'+str(list(authors))+'\t'+'None'+'\t'+'None')
                        #print '#######5######'