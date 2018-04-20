#!usr/bin/python
#coding: utf-8
#根据blast2nr的xml结果，解析成csv格式之后，统计subject description中的种属信息
#每个query对应的10个hit中，subject description中的一个种属只统计一次

import re

f1 = open('top10_subject_description_out.csv', 'r')
f2 = open('statistic_subject_description.csv', 'w')

lines = f1.readlines()
kinds_genus_list = []
num_genus_list = []

#逐个搜索每个query
for i in range(1, 790):
	query_list = []
	for line in lines:
		queryid = line.split(',')[0]
		if 'Query_%s'%i == queryid:
			genuses = re.findall(r"(\[.*?\])",line, re.M) #找出所有[]内的信息
			for genus in genuses:
				genus = genus.replace('[','').replace(']','') # 去除[]
				if 'Candidatus' in genus:
					genuss = genus.split(' ')[1] 
				else:
					genuss = genus.split(' ')[0]
					if genuss not in query_list: #每个queryID的10个hit subject description中的所有种属，每类只计数一次。
						query_list.append(genuss)
					if genuss not in kinds_genus_list:
						kinds_genus_list.append(genuss)
	for genus in query_list:
		num_genus_list.append(genus)
		#print genus

#统计每个分类的数量并写出到文件
for genus in kinds_genus_list:
	print genus
	num = num_genus_list.count(genus)
	print num
	f2.write(genus+','+str(num)+'\n')

f1.close()
f2.close()



