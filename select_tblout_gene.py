#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***
# 根据hmmsearch的输出结果,从ORF文件中将相应得基因序列抽提出来

f1 = open('../12accumu_orf_pro.fasta', 'r')
f2 = open('Ftsz_gene', 'r')
f3 = open('Ftsz_gene.fasta','w')

genelist = f1.read().split('>')
pfamlist = f2.readlines()

for line in pfamlist:
	genename = line.split(' ')[0]
	print genename
	for gene in genelist:
		if genename in gene:
			f3.write('>'+gene)
f1.close()
f2.close()
f3.close()
