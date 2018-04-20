#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***


f1 = open('31.32_major_70%_filter.blastp','r')
f2 = open('31.32_exclude_core_pro.fasta', 'r')
f3 = open('31.32_major_pro.fasta','w')
f4 = open('31.32_exclude_major_pro.fasta', 'w')

corelist = f1.readlines()
seqlist = f2.read().split('>')

core = []
for line in corelist:
	name = line.split('\t')[0]
	if name not in core:
		core.append(name)

core_add = []
for name in core:
	for line in corelist:
		if name in line:
			cluster = line.split('\t')[1].split('_')[0]
			ortholog = line.split('\t')[1].split('_')[1]
			full_name = cluster+'_'+ortholog+'_|_'+name
			if full_name not in core_add:
				core_add.append(full_name)
			break

exclude = []	
for full_name in core_add:
	for seq in seqlist:
		seqname = seq.split('\n')[0]
		s = '\n'.join(seq.split('\n')[1:])
		if seqname in full_name and s.strip() != '':
			f3.write('>'+full_name+'\n'+s)

for seq in seqlist:
	seqname = seq.split('\n')[0]
	if seqname not in core:
		f4.write('>'+seq)

f1.close()
f2.close()
f3.close()
f4.close()
