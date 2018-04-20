#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 从MCL的聚簇结果中抽出第一个簇的基因序列

f1 = open('../4.0.mcl/out.rhodo.mci.I13', 'r')
f2 = open('../accumu19_pro_good.faa', 'r')
f3 = open('I13_second_ortholog_seq.fasta', 'w')

orthologs = f1.readlines()
genes = f2.read().split('>')

n=0
for line in orthologs:
	n+=1
	if n==2:
		genenames = line.split('\t')
		for gene in genes:
			for name in genenames:
				if name in gene:
					f3.write('>'+gene)
	elif n>2:
		break

f1.close()
f2.close()
f3.close()
