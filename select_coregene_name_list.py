#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

# select gene sequence of coregene or species-specific gene.
import re

f1 = open('accumu8_coregene.cluster90-100%', 'r')
f2 = open('accumu8.coregene_name_list', 'w')

accumulist = []

for line in f1:
	genes = line.split('\t')
	for gene in genes:
		if 'JEMY' in gene:
			accumulist.append(gene)

for a in accumulist:
	f2.write(a+'\n')
	
f1.close()
f2.close()
