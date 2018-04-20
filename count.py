#! /usr/bin/env python
# -*- coding: utf-8 -*-

f1 = open('identi60_keylist_unique', 'r')
f2 = open('genome_unique_gene_count', 'w')

genelist = f1.readlines()
uniquelist = set(genelist)

for genome in uniquelist:
	num = genelist.count(genome)

	f2.write(genome.strip()+'\t'+str(num)+'\n')
