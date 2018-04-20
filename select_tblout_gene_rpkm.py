#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***
# 根据hmmsearch的输出结果,从ORF文件中将相应得基因序列抽提出来

f1 = open('../accumu5_two_metatrans_cov.csv', 'r')
f2 = open('ppk_gene_name.txt', 'r')
f3 = open('ppk1_rpkm.csv','w')

rpkmlist = f1.readlines()
pfamlist = f2.readlines()

for line in pfamlist:
	#genename = line.split(' ')[0]
	for rpkm in rpkmlist:
		if line in rpkm:
			f3.write(rpkm)
f1.close()
f2.close()
f3.close()