#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

f1 = open('../accumu19_pro.faa', 'r')
f2 = open('query_unique.txt', 'r')
f3 = open('accumu19_pro_good.faa', 'w')


genelist = f1.read().split('>')
querylist = f2.readlines()

for gene in genelist:
	genename=gene.split('\n')[0]

	if 'partial=00' in gene:
		f3.write('>'+gene)
	else:
		for query in querylist:
			#print query
			if genename == query.strip():
				f3.write('>'+gene)
	
f1.close()
f2.close()
f3.close()
