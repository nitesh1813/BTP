
f1=open('/home/nitesh/Downloads/BTP/reject/singlerej','r')
mp={}
for line in f1:
	# line=lines.split(',')
	# print line
	# # mp.append(line)
	# mp[int(line[0])]=line[1].strip('"').rstrip("\n")
	mp[line.rstrip('\n').lower()]=0
count=0
print len(mp)
countfalse=0
lists={}
f1=open('/home/nitesh/Downloads/BTP/vers','r')
# f2=open('/home/nitesh/Downloads/BTP/Accepted/acceptedsingle','r')
fmul=open('/home/nitesh/Downloads/BTP/reject/singrejsid','w')
# fsin=open('/home/nitesh/Downloads/BTP/Accepted/singletitle','w')


# for line in f1:
# 	if int(line.rstrip('\n')) in mp:
# 		print>>fmul,mp[int(line.rstrip('\n'))]

# for line in f2:
# 	if int(line.rstrip('\n')) in mp:
# 		print>>fsin,mp[int(line.rstrip('\n'))]		

for line in f1:
	# print line
	lines=line.split("|")
	if lines[0].lower() in mp:
		lists[lines[0]]=[]
		print>>fmul, lines[1].rstrip('\n')
		lists[lines[0]].append(lines[1].rstrip("\n"))
		# mp[lines[0]].append(lines[1]);
		count=count+1
# f1=open('/home/nitesh/Downloads/BTP/jstat_titles_failedtwice','r')
# for line in f1:
# 	if line in mp:
# 		mp[line]=2;
# 		countfalse=countfalse+1		
print count
# f1=open('/home/nitesh/Downloads/BTP/scopusids','w')
# f2=open('/home/nitesh/Downloads/BTP/jstat_titles_successmatch','w')

# for line in lists:
# # 	if mp[line]==2:
# # 		print >>f1,line

# 	print >> f1,lists[line][0]

