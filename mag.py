import httplib, urllib, base64
import requests
import json

import os
fbad=open("/home/nitesh/Downloads/BTP/failedmicrosoft",'w')
os.environ['http_proxy']="http://10.3.100.207:8080"
# headers = {
#     # Request headers
#     'Ocp-Apim-Subscription-Key': '1b9dc9755e204ab98084633123bbf88d',
# }
# https://api.projectoxford.ai/academic/v1.0/interpret?query=papers by jaime&complete=1&count=2


# https://oxfordhk.azure-api.net/academic/v1.0/interpret?query=bill&subscription-key=6db05be087954451b70bed69847bd9dc
# https://oxfordhk.azure-api.net/academic/v1.0/interpret?query=bill&subscription-key=6db05be087954451b70bed69847bd9dc
# https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Ti=%27the%20dynamics%20of%20viral%20marketing%27&attributes=Ti,Y,CC,AA.AuN,AA.AuId&subscription-key=6db05be087954451b70bed69847bd9dc
# print "lol    "
# conn.request("GET", "/academic/v1.0/evaluate?%s" % params, headers)
def getdata(title):
        # urllib2.urlopen('oxfordhk.azure-api.net/academic/v1.0/interpret?query=bill&subscription-key=6db05be087954451b70bed69847bd9dcd').read()
        # titlse="Note on the Jarzynski Equality"
        # title="the%20dynamics%20of%20viral%20marketing"
    try:    
        query="https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Ti='"+title+"'&attributes=Ti,Y,CC,AA.AuN,AA.AuId&subscription-key=6db05be087954451b70bed69847bd9dc"
        # conn = httplib.HTTPSConnection('oxfordhk.azure-api.net').request("GET",query)
        # print query
        resp = requests.get(query)
        data=json.loads(resp.text.encode('utf-8'))
        print "lol    "
        # conn.request("GET", "/academic/v1.0/interpret?%s" % params,'{body}', headers)
        # conn.request("GET","/academic/v1.0/interpret?query=booksbyjames&subscription-key=6db05be087954451b70bed69847bd9dc")
        print "no"
        # print data
        # response = conn.getresponse()
        # data = response.read()
        if len(data[u'entities']) ==0:
            print "title"
        else:
            print>> fbad, data    
        # conn.close()
    except Exception as e:
        pass
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))
        # print>> fbad, title

f=open("/home/nitesh/Downloads/BTP/jstat_title",'r')
for line in f:
    getdata(line.rstrip("\n").lower())