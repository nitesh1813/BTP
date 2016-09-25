import requests
import json
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib
import lxml.html
import time
total=0
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Firefox()
mp = []

def wait_until_visible_then_click(element):
    element = WebDriverWait(browser,5,poll_frequency=.2).until(EC.visibility_of(element))
    element.click()
def correct_url(url): 
	if not url.startswith("http://") and not url.startswith("https://"):
  		url = "http:" + url
 	return url

def scrollDown(browser, numberOfScrollDowns):
	body = browser.find_element_by_tag_name("body")
 	while numberOfScrollDowns >=0:
  		body.send_keys(Keys.PAGE_DOWN)
  		numberOfScrollDowns -= 1
 	return browser
def crawl_url(url, run_headless=True):
	if run_headless:
  		display = Display(visible=0, size=(1024, 768))
  		display.start()

	url = correct_url(url)
	
	
	
	i=0
	#browser = webdriver.Firefox()
	global browser
	global fileinfo
	browser.get(url)
	# time.sleep(3)
	# browser=scrollDown(browser,2)
	time.sleep(2)
	
	browsers=browser
	
	i=0
	
	
	for i in range(50):

		try:
			soup = BeautifulSoup(browser.page_source)
			x=y=z=date=[]
			x=soup.findAll('div',{'id':'resultsBody'})
			y=soup.findAll('div',{'id':'resultDataRow0'})
			z=soup.findAll('a',{'title':'Show document details'})
			date=soup.findAll('div',{'class':'dataCol4'})
			# print date
			# for year in date:
			# 	print year.span.text
			f1=open(fileinfo,"a")
			a=soup.findAll('a',{'title':'Show author details'})
			for tags,year in zip(z,date):
				print>>f1, tags.text+", "+year.span.text.strip("\n")
			try:
				browser.find_element_by_xpath('//*[@title="Next page"]').click()
			except:
				i=51
				print"no next page"
					
	
		except:
			i=51	
			print i
			print "some error"
			


fileinfo=""
# from my_scopus import MY_API_KEY
def getuser(title):
	global fileinfo
	# url = ("http://api.elsevier.com/content/abstract/scopus_id/00"
	# 	+str(id)
	#           + "?field=authors,title,publicationName,volume,issueIdentifier,"
	#           + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
	# paper_info_search = requests.get(api_resource + 'query=doi(10.1016/j.fusengdes.2015.04.018)', headers=headers) 

	url="http://api.elsevier.com/content/search/scopus?query=title("+title+")"
	resp = requests.get(url,
	                    headers={'Accept':'application/json',
	                             'X-ELS-APIKey': '3fc3331c78581078daf7e2b97f3c252b'})
	
	result = json.loads(resp.text.encode('utf-8'))
	# print result
	test= result['search-results']['entry']
	# print test
	SCOPUS_ID= test[0]['dc:identifier']
	return SCOPUS_ID
	# print SCOPUS_ID
	# url="https://api.elsevier.com/content/abstract/citations?s"
	# link=test[0]['link'][3]['@href']
	# f3=open("/home/nitesh/Downloads/BTP/jstat_citers","a")
	# print>>f3, link
	# crawl_url(link)
	# print link['@href']
	# fileinfo="/home/nitesh/Downloads/BTP/new_jsats/"+SCOPUS_ID
	# # print fileinfo
	# # return link[10:]
	# url = ("http://api.elsevier.com/content/abstract/scopus_id/"
 #          + SCOPUS_ID
 #          + "?field=authors,title,publicationName,volume,issueIdentifier,"
 #          + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
	# newresp = requests.get(url,
	#                     headers={'Accept':'application/json',
	#                              'X-ELS-APIKey': '3fc3331c78581078daf7e2b97f3c252b'})
	# results = json.loads(newresp.text.encode('utf-8'))
	# authors=""
	# for au in results['abstracts-retrieval-response']['authors']['author']:
	# 	authors=authors+ au['ce:indexed-name'] +","
	# # for res in results['abstracts-retrieval-response']['authors']
	# # 	print res+"-----------"

	
	# fstring= '({cites}).\n'
	# lol=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8'))
	# return lol
	# lol= fstring.format(date=results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8'),
 #                        cites=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')))
	# lol= lol
	                 
	# newresults = json.loads(resp.text.encode('utf-8'))
	
	# fstring = '{authors}'
	# return fstring.format(authors=','.join([au['ce:indexed-name'] for au in results['abstracts-retrieval-response']['authors']['author']])

i=0
f=open("/home/nitesh/Downloads/BTP/jstat_title",'r')
fail=open("/home/nitesh/Downloads/BTP/jstat_titles_failedthrice",'w')
fileinfo="/home/nitesh/Downloads/BTP/vers"
f1=open(fileinfo,"w")
for title in f:
 	# titlesplit=title.split(",")
 	# tit=titlesplit[1].strip('"')
 	# print titlesplit[0]
 	# print tit
 	try:
		info= getuser(title)
		print info

		# print fileinfo
		
		print>> f1,title+","+info
		print "done"
	except:
		# pass

		# print es
		print >> fail,title

		# os.remove(fileinfo)