#!usr/bin/python
#coding: utf-8
#根据blast2nr的xml结果，解析成csv格式之后，统计subject description中的种属信息

import re

f1 = open('top10_out.csv', 'r')
f2 = open('subject_description_out.csv', 'w')

lines = f1.readlines()
kinds_genus_list = []
num_genus_list = []


for line in lines:
	genuses = re.findall(r"(\[.*?\])",line, re.M)
	for genus in genuses:
		#print genus
		genus = genus.replace('[','').replace(']','')
		num_genus_list.append(genus)
		if genus not in kinds_genus_list:
			kinds_genus_list.append(genus)

for genus in kinds_genus_list:
	print genus
	num = num_genus_list.count(genus)
	print num
	f2.write(genus+','+str(num)+'\n')

f1.close()



