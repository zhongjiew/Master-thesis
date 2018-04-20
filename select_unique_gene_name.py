#! /usr/bin/env python
# -*- coding: utf-8 -*-
# this script aims to select genes present in more than 90% genomes, 
# which named core genes.

f1 = open('out.rhodo.mci.I11', 'r')
f2 = open('unique.gene.cluster0-10%', 'w')
f3 = open('keylist_0-0%', 'w')

ortholog = f1.readlines()
keylist = []

for eachline in ortholog:
	genes = eachline.split('\t')
	for gene in genes:
		if "gi|" in gene:
			keyword = gene.split('|')[3][:6]
		else:
			keyword = gene.split('_')[0]
			
		if keyword not in keylist:
			keylist.append(keyword)

	num = len(keylist)
	if num < 2: 	#change the genome number to obtain all(100%:42)/core(90%:38)/major(50%:21)/unique(1) genes.
		for key in keylist:
			f3.write(key+'\t')
		f3.write('\n')
		print num
		f2.write(eachline)
	keylist = []

f1.close()
f2.close()
f3.close()
