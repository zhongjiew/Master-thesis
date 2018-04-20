#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Author: zhongjie wang
#根据三个B level下面同源簇的名称，将对应的5个基因组的RPKM值提取出来


f1 = open('accumu5_pan_single_copy_pro.fasta', 'r')
f2 = open('../3b_level_all_orthologs.txt', 'r')
f3 = open('3b_level_ortholog_pro.fasta', 'w')

seqlist = f1.read().split('>')
ortholist = f2.readlines()
for row in ortholist:
	row = row.strip()
	for line in seqlist:
		name = line.split('\n')[0].split('_|_')[0]
		if row == name:
			f3.write('>'+line)