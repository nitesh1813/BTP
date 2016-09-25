#get file from folder
f=open("/home/nitesh/Downloads/BTP/reject/singrejsid",'r')
out=open("/home/nitesh/Downloads/BTP/reject/rejectsingstats",'w')

for file in f:
	try:
		item=open("/home/nitesh/Downloads/BTP/jstat_titles/"+file.rstrip("\n"),'r')
		for line in item:
			if 'cited' in line : 
				count=line.split(",")[1]
				print>> out,file.rstrip("\n"), count[8:len(count)-9]
	except:
		pass			

# make plot
# get stats 


