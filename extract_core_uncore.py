#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

f1 = open('bin2_rare_50%_filter.blastp','r')
f2 = open('bin2_exclude_major_pro.fasta', 'r')
f3 = open('bin2_rare_pro.fasta','w')
f4 = open('bin2_exclude_rare_pro.fasta', 'w')

core = []
corelist = f1.readlines()
for line in corelist:
	name = line.split('\t')[0]
	if name not in core:
		core.append(name)

seqlist = f2.read().split('>')	
for seq in seqlist:
	seqname = seq.split('\n')[0]
	if seqname in core:
		f3.write('>'+seq)
	else:
		f4.write('>'+seq)

f1.close()
f2.close()
f3.close()
f4.close()
