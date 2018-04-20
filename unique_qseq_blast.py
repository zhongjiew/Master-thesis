#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: zhongjie wang ***
#将比对到同一个marker的query进行unique

import sys
f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')

genelist = f1.readlines()

qseqlist = []
for line in genelist:
	qseq = line.split('\t')[0]
	if qseq not in qseqlist:
		qseqlist.append(qseq)

relationlist = []
for qseq in qseqlist:
	for line in genelist:
		maker = line.split('\t')[1].split('_')[0]
		other = '\t'.join(line.split('\t')[2:])
		if qseq in line:
			relation = qseq+'\t'+maker
			print relation
			if relation not in relationlist:
				relationlist.append(relation+'\t'+other)
				
for relation in relationlist:
	f2.write(relation)

f1.close()
f2.close()