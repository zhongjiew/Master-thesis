#! /usr/bin/env python
#zhongjie wang
#2018/04/11
#提取某一类基因，只需在keyword后面写上需要提取的关键词


f1 = open('key.txt', 'r')
f2 = open('35-42I20', 'w')
keyword = " "

genelist = f1.read().split('>')
for gene in genelist:
	if keyword in gene:
		f2.write('>'+gene)

f1.close()
f2.close()