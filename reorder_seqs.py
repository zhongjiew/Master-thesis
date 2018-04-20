#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***
# 根据基因组名称关键字去匹配基因名称，如果能匹配上，则将基因抽提出来，
# 如果匹配不上，则将基因组名称关键字作为基因名称，空一行作为序列

import re

for i in range(1, 672):
	f1 = open('key.txt', 'r')
	f2 = open('../psc_cluster_file/ortholog%s.fasta'%i, 'r')
	f3 = open('ortholog_sorted%s.fasta'%i,'a')

	cluster_keylist = []

	for genes in f2:
		if genes.startswith('>'):
			keyname = genes[1:-1]
			cluster_keylist.append(keyname)

	f2 = open('../psc_cluster_file/ortholog%s.fasta'%i, 'r')

	keylist = f1.read().split('\t')
	genelist = f2.read().split('>')

	for key in keylist:
		names = '\t'.join(cluster_keylist)
		if key in names:
			for gene in genelist:
				if key in gene:
					f3.write('>'+gene)
					break
		else:
			f3.write('>'+key+'\n'+'\n')
	f1.close()
	f2.close()
	f3.close()
