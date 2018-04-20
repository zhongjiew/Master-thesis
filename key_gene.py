#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: zhongjie wang ***
#根据key gene列表统计出prokka对每个基因组注释结果中的key gene的locus tag以及数量
#f1输入key gene文件，f2输入prokka注释结果tsv文件
#f3输出每个基因组key gene的locus tag，f4输出每个基因组每个key gene的数量

import re
import os
import sys

currentpath = os.getcwd()
path = '%s/tsv/' %currentpath
filelist = os.listdir(path)


f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')
f3 = open(sys.argv[3], 'w')
#f4 = open(sys.argv[4],'w')

keygenes = f1.readlines()

for filename in filelist:
	binname = filename.replace('.tsv', '')
	f2.write('\t'+binname)
	f3.write('\t'+binname)
f2.write('\n')
f3.write('\n')

for keygene in keygenes:
	kg_name, key = keygene.split(',')[0:2]
	f2.write(kg_name+'('+key+')'+'\t')
	f3.write(kg_name+'\t')
	for filename in filelist:
		#if not os.path.isdir(file):
		file = open(path+filename, 'r')
		lines = file.readlines()
		n = 0
		for line in lines:
			line = line.split('\n')
			for col in line:
				if 'CDS' in col:
					genelocus = col.split('\t')[0]
					cds = col.split('\t')[1]
					key1 = col.split('\t')[2]
					if re.match(key.strip(), key1.strip()):
						n += 1
						f2.write(genelocus+';')
		f2.write('\t')
		f3.write(str(n)+'\t')
	f2.write('\n')
	f3.write('\n')


