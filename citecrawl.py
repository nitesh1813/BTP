# html_doc="https://www.scopus.com/inward/citedby.uri?partnerID=HzOxMe3b&scp=34547695083&origin=inward"
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
import re
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
def crawl_url(url,scpid, run_headless=True):
	if run_headless:
  		display = Display(visible=0, size=(1024, 768))
  		display.start()

	url = correct_url(url)
	print url
	# t = lxml.html.parse(url)
	# title= t.find(".//title").text
	# print title
	# global mp
	# mp.append(url)
	i=0
	#browser = webdriver.Firefox()
	global browser
	
	browser.get(url)
	# time.sleep(3)
	# browser=scrollDown(browser,2)
	time.sleep(2)
	# while i<3:
	# 	try:
	# 		i=i+1
	# 		try:
	# 			browser.find_element_by_id("Col1-2-Comments").click()
	# 		except:
	# 			print "error"
	# 		print "clicked"
	# 		time.sleep(2)
	# 	except:
	# 		break
		
	# browser=scrollDown(browser,5)
	# browsers=browser
	
	i=0
	f1=open("/home/nitesh/Downloads/BTP/jstat_cites/"+scpid,"w")
	soup = BeautifulSoup(browser.page_source)
	flag=0
	for i in range(50):
		try:
			

			# x=soup.findAll('div',{'id':'resultsBody'})
			# y=soup.findAll('div',{'id':'resultDataRow0'})
			if flag==0:
				z=soup.findAll('a',{'title':'Show document details'})
				date=soup.findAll('div',{'class':'dataCol4'})
				# print year.span.text
				a=soup.findAll('a',{'title':'Show author details'})
				for tags,year in zip(z,date):
					print>> f1, tags.text+", "+year.span.text.strip("\n")
					# print i
				# print tags.text+", "+year.span.text.strip("\n")
			try:
				browser.find_element_by_xpath('//*[@title="Next page"]').click()
				soup = BeautifulSoup(browser.page_source)
			except:
				flag=1
				print i
				return
				



			
		except:
			flag=1
			print "some error"
			return
			i=51	
		i=i+1


	

if __name__=='__main__':
	f=open("/home/nitesh/Downloads/BTP/jstat_citers","r")
	for link in f:
		match = re.search(r'scp=?([^&>]+)', link)
		
		scpid=match.group(1)
		print scpid
		# html_doc="https://www.scopus.com/inward/citedby.uri?partnerID=HzOxMe3b&scp=84900631115&origin=inward"
		crawl_url(link,scpid)
