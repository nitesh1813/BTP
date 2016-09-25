f1=open('/home/nitesh/Downloads/BTP/multireviews.csv','r')

f2=open('/home/nitesh/Downloads/BTP/versioncites','r')
mp={}
count=0


for lines in f1:
	# mp.append(line)
	line=lines.split(" ")
	# print line[0]
	mp[int(line[0])]=0
	count=count+1
# for line in mp:
countfalse=0
for lines in f2:
	line=lines.split(" ")
	print line[0]
	if int(line[0]) in mp:	
		mp[line[0]]=line[1];
		
# 	print line,mp[line]		
# f1=open('/home/nitesh/Downloads/BTP/jstat_titles_failedtwice','r')
# for line in f1:
# 	if line in mp:
# 		mp[line]=2;
# 		countfalse=countfalse+1		
print count	,countfalse
# f1=open('/home/nitesh/Downloads/BTP/jstat_titles_failedmatch','w')
# f2=open('/home/nitesh/Downloads/BTP/jstat_titles_successmatch','w')

# for line in mp:
# 	if mp[line]==2:
# 		print >>f1,line
# 	if mp[line]==1:
# 		print >> f2,line	

