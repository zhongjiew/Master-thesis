#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

f1 = open('accumu6_orf_nuc_good.fasta','r')
f2 = open('31.32_orf_nuc_good.fasta', 'w')
f3 = open('1.2.3.26_orf_nuc_good.fasta', 'w')

gene_nucs = f1.read().split('>')
#gene_nucs = f2.read().split('>')

for gene_nuc in gene_nucs:
	if "Bin31.4" in gene_nuc or "Bin32.1" in gene_nuc:
		f2.write(">"+gene_nuc)
	else:
		f3.write(">"+gene_nuc)


f1.close()
f2.close()
f3.close()
