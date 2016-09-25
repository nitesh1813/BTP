from bs4 import BeautifulSoup
import codecs
import io
import re
import os
from os.path import isfile, join
import glob
# print glob.glob("/home/nitesh/Downloads/BTP/*")
lol= os.listdir("/home/sandipan_nitesh/Downloads/responses/responses/")

for lo in lol:
	try:
		print "there"
		f=open("/home/sandipan_nitesh/Downloads/responses/results/"+lo,'w')
		print "here"
		html_doc=lo
		soup = BeautifulSoup(open(html_doc))
		print>> f,"Title :"+ soup.title.string
		desc= soup.find(attrs={'name':'citation_publication_date'})
		print>> f,"Date Of Publication :"+ desc['content']


		auth=soup.find_all("meta", {"name":"citation_author"})

		for aut in auth:
			print>> f, "Author :"+aut['content']
	except:
		print "error"		