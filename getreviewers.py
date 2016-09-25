import json
import os
mp={}
getdata=open("/home/nitesh/Downloads/BTP/fulldata.txt")
mas=0

for line in getdata:
	lists=line.split(',')
	# 
	# print lists[0]
	if mas<int(lists[0]):
		mas=int(lists[0])
	else:
		pass	
	if int(lists[0]) in mp:
		if int(lists[1]) in mp[int(lists[0])]:
			if lists[3]!='None':
				if lists[3] in mp[int(lists[0])][int(lists[1])]:
					mp[int(lists[0])][int(lists[1])][lists[3]].append(int(lists[5]))
				else:
					mp[int(lists[0])][int(lists[1])][lists[3]]=[]
					mp[int(lists[0])][int(lists[1])][lists[3]].append(int(lists[5]))
			else:
					
				if lists[2] in mp[int(lists[0])][int(lists[1])]:
					mp[int(lists[0])][int(lists[1])][lists[2]].append(int(lists[5]))
				else:
					mp[int(lists[0])][int(lists[1])][lists[2]]=[]
					mp[int(lists[0])][int(lists[1])][lists[2]].append(int(lists[5]))

					
				

		else:
			mp[int(lists[0])][int(lists[1])]={}
			if lists[3]!='None':
				mp[int(lists[0])][int(lists[1])][lists[3]]=[]
				mp[int(lists[0])][int(lists[1])][lists[3]].append(int(lists[5]))
			# mp[lists[0]][lists[1]].append(int(lists[5]))
	else:
		mp[int(lists[0])]={}
		mp[int(lists[0])][int(lists[1])]={}
		if lists[3]!='None':
			mp[int(lists[0])][int(lists[1])][lists[3]]=[]
			mp[int(lists[0])][int(lists[1])][lists[3]].append(int(lists[5]))
counts=0
f1=open("/home/nitesh/Downloads/BTP/multiplereviewrsdocuments.txt","w")
f2=open("/home/nitesh/Downloads/BTP/singledoc.txt","w")
for key in mp:
	flag=0
	for lis in mp[key]:

		# if flag==0:
		count=0
		temp=[]
		for fin in mp[key][lis]: 
			if 2 in mp[key][lis][fin]:
				count=count+1
				temp.append(int(fin))
				# print key,lis,fin,mp[key][lis][fin]	
		if count>1:
			# print key,lis,temp
			flag=1
	counts=counts+1			
	if flag==1:
		print >>f1,key
		
	else:
		print>>f2,key	
			# elif count==1:
			# 	# print>>f2,key,lis,temp
			# 	counts=counts+1
		# flag=1					
# 	print key?
print counts
