#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Author: zhongjie wang
#根据三个B level下面同源簇的名称，将对应的5个基因组的RPKM值提取出来


f1 = open('accumu5_single_copy_good_rpkm_func.csv', 'r')
f2 = open('3b_level_all_orthologs.txt', 'r')
f3 = open('3b_level_ortho_rpkm1_2_func.csv', 'w')

funclist = f1.readlines()
ortholist = f2.readlines()

for line in funclist:
	ortho = line.split(',')[0]
	rpkm = line.split(',')[1:12]
	func = line.split(',')[13].split(' [')[0]
	for row in ortholist:
		row = row.strip()
		if row in line:
			f3.write(func+','+line)