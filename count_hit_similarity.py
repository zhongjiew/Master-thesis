#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

import re

f1 = open('uw1_blast2rhodo93.blastp.filter.19hit', 'r')
f2 = open('uw1_blast2rhodo93.blastp.46hit_count.tsv', 'w')

hits = f1.readlines()
ori_qseqlist = []

for line in hits:
	qseq = line.split('\t')[0]
	ori_qseqlist.append(qseq)

qseqlist = []
for line in hits:
	qseq = line.split('\t')[0]
	if qseq not in qseqlist:
		qseqlist.append(qseq)

for i in range(0, 25):
	f2.write('\t'+'Section[%d'%(50+2*i)+'-%d)'%(50+2*(i+1)))
f2.write('\n')

n = 0
for qseq in qseqlist:
	n += 1
	f2.write('Ortholog%04d'%n)
	num = 0
	hit_num=ori_qseqlist.count(qseq)
	for i in range(0, 25):
		for hit in hits:
			pident = hit.split('\t')[2]
			if qseq in hit:
				if 	int(50+2*i) <= float(pident) < int(50+2*(i+1)):
					num += 1
		f2.write('\t'+str(float(num)/hit_num))
	f2.write('\n')

f1.close()
f2.close()
