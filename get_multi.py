f=open("/home/nitesh/Downloads/BTP/multireviewers.csv",'r')
f1=open("/home/nitesh/Downloads/BTP/singlereview",'w')
f2=open("/home/nitesh/Downloads/BTP/multireviews.csv",'w')

reviewss={}
for line in f:
	lines=line.split(',')
	if lines[1] in reviewss:
		reviewss[lines[1]].append(lines[4])
	else:
		reviewss[lines[1]]=[]
		reviewss[lines[1]].append(lines[4])


for key in reviewss:
	if len(reviewss[key])==1:
		print>> f1, key,reviewss[key]
	else:
		print>>f2, key,reviewss[key]	