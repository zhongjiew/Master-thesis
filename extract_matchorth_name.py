#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang***

### this script aims to extract orthologous gene cluster names according to match result key_match_orth.py genetated. ###

f1 = open('key.txt', 'r')
f2 = open('out.rhodo.mci.I11', 'r')
f3 = open(r'core_gene_cluster','w')

keylist = f1.read().split('\t')
orth = f2.readlines()

for eachline in orth:
		b = 0
		arr = eachline.strip('\n')
		for key in keylist:
			a = arr.count(key)
			if a > 1:
				b += 1
			else:
				b += a
		if b >= 9:
			f3.write(eachline)
		
f1.close()
f2.close()
f3.close()
