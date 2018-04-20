#! /usr/bin/env python
# -*- coding: utf-8 -*-
# how many genes of each genome belong to each category 

f1 = open('genome_unique_gene_annotation.txt', 'r')
f2 = open('unique_gene_subsystems.tsv', 'r')
f3 = open('uw1_hyprotein_.txt', 'w')

genelist = f1.readlines()

#generate gene annotation dict
mydict1=defaultdict(dict)
a = 0
for lines in genelist:
	a += 1
	if a >1:
		lines=lines.strip('\n')
		genome, feaid = lines.split('\t')[0:2]
		hypo = lines.split('\t')[7]
		if genome.startswith('gi'):
			g=genome.split('|')[3][0:6]
		else:
			g=genome.split('_')[0]

		if mydict1.get(g):
			mydict1[g].append('\t\t'.join([feaid,hypo]))
		else:
			mydict1[g]=[]
			mydict1[g].append('\t\t'.join([feaid,hypo]))




f1.close()
f2.close()
f3.close()
f4.close()