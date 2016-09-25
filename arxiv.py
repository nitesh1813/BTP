import urllib
f=open('/home/nitesh/Downloads/BTP/arxivmatched','w')
def gettitles(query):
	try:

		url = 'http://export.arxiv.org/api/query?search_query=all:'+query+'&max_results=1'
		data = urllib.urlopen(url).read()
		title = str(data).split('<title>')[1].split('</title>')[0]
		print>> f, title
	except:
		pass	


f1=open('/home/nitesh/Downloads/BTP/jstat_titles_failedmatch','r')
for line in f1:
	gettitles(line.rstrip('\n'))