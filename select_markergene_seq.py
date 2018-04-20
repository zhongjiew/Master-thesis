#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***
#将marker基因按照一定的基因组顺序提取出来，并且每个Marker所包含的基因生成一个文件

import re

f1 = open('gnm23_pro.fasta', 'r')
f2 = open('final_good_qseq.txt', 'r')
f3 = open('marker.txt', 'r')
f4 = open('genome.txt', 'r')

seqlist = f1.read().split('>')
good_qseqlist = f2.readlines()
markerlist = f3.readlines()
genomelist = f4.readlines()

for marker in markerlist:
	marker=marker.strip()
	marker_seqs, genome_name =[],[]
	f5 = open('%s.faa'%marker, 'w')
	for good_qseq in good_qseqlist:
		qseqname,qmarker = good_qseq.split('\t')[:2]
		#print qseqname, qmarker
		if marker == qmarker.strip():
			genome_name.append(qseqname)
			for seq in seqlist:
				if qseqname in seq:
					marker_seqs.append(seq)


	keys = '\t'.join(genome_name)
	for genome in genomelist:
		genome = genome.strip()
		if genome in keys:
			print genome
			for seq in marker_seqs:
				if genome in seq:
					f5.write('>'+seq)
		else:
			f5.write('>'+genome+2*'\n')

	f5.close()

f1.close()
f2.close()
f3.close()
f4.close()
