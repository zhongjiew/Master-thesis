#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

f1 = open('../1.rm_redundance/query_unique.txt','r')
f2 = open('../../2.0.prodigal/accumu6_orf_pro.fasta','r')
f3 = open('accumu6_orf_pro_good.fasta', 'w')

ortholog = f1.readlines()
gnm_contigs = f2.read().split('>')
keylist = []

for eachline in ortholog:
	if eachline not in keylist:
		keylist.append(eachline.strip())

for contigs in gnm_contigs:
	contig_name = contigs.split('\n')[0]
	if '*' in contigs and "=Edge" not in contigs or contig_name in keylist:
		f3.write(">"+contigs)
	else:
		pass


f1.close()
f2.close()
f3.close()
