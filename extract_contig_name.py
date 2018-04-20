#! /usr/bin/env python
# -*- coding: utf-8 -*-
# this script aims to select genes present in more than 90% genomes, 
# which named core genes.

f1 = open('core_gene_cluster', 'r')
f2 = open('UW-1.fasta', 'r')
f3 = open('UW-1_good.fasta', 'w')
f4 = open('UW-1_excluted.fasta', 'w')

ortholog = f1.readlines()
gnm_contigs = f2.read().split('>')
keylist = []

for eachline in ortholog:
	core_contigs = eachline.split('\t')
	for core_contig in core_contigs:
		core_contig = core_contig.split('_')[:-1]
		core_contig = '_'.join(core_contig)
		if core_contig not in keylist:
			keylist.append(core_contig)

for contigs in gnm_contigs:
	contig_name = contigs.split('\n')[0].split(' ')[0]
	if contig_name in keylist:
		f3.write(">"+contigs)
	else:
		f4.write(">"+contigs)


f1.close()
f2.close()
f3.close()
