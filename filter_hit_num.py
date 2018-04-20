#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

# select gene sequence of coregene or species-specific gene.
import re

f1 = open('uw1_blast2rhodo93.blastp.filter', 'r')
f2 = open('uw1_blast2rhodo93.blastp.filter.19hit', 'w')

hits = f1.readlines()
qseqlist = []
ori_qseqlist = []

for line in hits:
	qseq = line.split('\t')[0]
	ori_qseqlist.append(qseq)

for line in hits:
	qseq = line.split('\t')[0]
	if qseq not in qseqlist:
		qseqlist.append(qseq)

qseq_goodlist = []
for qseq in qseqlist:
	num = ori_qseqlist.count(qseq)
	print num
	if num > 18:
		qseq_goodlist.append(qseq)

for qseq in qseq_goodlist:
	for hit in hits:
		if qseq	in hit:
			f2.write(hit)
	
f1.close()
f2.close()
