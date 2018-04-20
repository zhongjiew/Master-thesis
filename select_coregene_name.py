#! /usr/bin/env python
# -*- coding: utf-8 -*-
# this script aims to select genes present in more than 90% genomes, 
# which named core genes.

f1 = open('out.rhodo.mci.I11', 'r')
f2 = open('coregene.cluster90-100%', 'w')
f3 = open('keylist_90-100%', 'w')

ortholog = f1.readlines()
keylist = []

for eachline in ortholog:
	genes = eachline.split('\t')
	#print gene
	for gene in genes:
		keyword = gene[:5]
		#print keyword
		if keyword not in keylist:
			keylist.append(keyword)

	num = len(keylist)
	if num >= 36:  	#change the genome number to obtain all(100%:42)/core(90%:38)/major(50%:21)/unique(1) genes.
		for key in keylist:
			f3.write(key+'\t')
		f3.write('\n')
		print num
		f2.write(eachline)
	keylist = []

f1.close()
f2.close()
f3.close()
