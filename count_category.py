#! /usr/bin/env python
# -*- coding: utf-8 -*-
# how many genes of each genome belong to each category 

from collections import defaultdict
import sys

f1 = open('genome_unique_gene_annotation.txt', 'r')
f2 = open('unique_gene_subsystems.tsv', 'r')
f3 = open('category_subcat_count_result.txt', 'w')
f4 = open('category_count_result.txt', 'w')

genelist = f1.readlines()
subsyslist = f2.readlines()

#generate gene annotation dict
mydict1=defaultdict(dict)
a = 0
for lines in genelist:
	a += 1
	if a >1:
		lines=lines.strip('\n')
		genome, feaid = lines.split('\t')[0:2]
		hypo = lines.split('\t')[7]
		if genome.startswith('gi'):
			g=genome.split('|')[3][0:6]
		else:
			g=genome.split('_')[0]

		if mydict1.get(g):
			mydict1[g].append('\t\t'.join([feaid,hypo]))
		else:
			mydict1[g]=[]
			mydict1[g].append('\t\t'.join([feaid,hypo]))


#generate subsystem dict
mydict2=defaultdict(dict)
b = 0
for rows in subsyslist:
	b += 1
	if b > 1:
		category,subcate = rows.split('\t')[0:2]
		feature = rows.split('\t')[4].strip('\n')
		if mydict2[category].get(subcate):
			mydict2[category][subcate].append(feature)
		else:
			mydict2[category][subcate]=[]
			mydict2[category][subcate].append(feature)



#output category and subcategory and sum file
f3.write('\t\t')
for g in mydict1:
	f3.write(g+'\t')
f3.write('\n')

for category in mydict2:
	f3.write(category+'\t')
	for subcate in mydict2[category]:
		f3.write(subcate+'\t')
		for g in mydict1:
			i = 0
			for features in mydict2[category][subcate]:
				feature = features.split(', ')
				for feat in feature:
					for items in mydict1[g]:
						feaid, hypo = items.split('\t\t')[0:2]
						if feaid == feat:
							i += 1
			f3.write(str(i)+'\t')
		f3.write('\n')
		f3.write('\t')
	f3.write('\n')

f3.write('Hypothetical protein'+'\t\t')
for g in mydict1:
	num = 0
	for items in mydict1[g]:
		feaid,hypo = items.split('\t\t')[0:2]
		if "hypothetical protein" in hypo:
			num += 1
	f3.write(str(num)+'\t')
f3.write('\n')

f3.write('No hit'+'\t'+'592'+'\n')



#output category and sum file
for g in mydict1:
	f4.write('\t'+g)
f4.write('\n')

for category in mydict2:
	f4.write(category+'\t')
	for g in mydict1:
		i = 0
		for subcate in mydict2[category]:
			for features in mydict2[category][subcate]:
				feature = features.split(', ')
				for feat in feature:
					for items in mydict1[g]:
						feaid, hypo = items.split('\t')[0:2]
						if feaid == feat:
							i += 1
		f4.write(str(i)+'\t')
	f4.write('\n')

f4.write('Hypothetical protein'+'\t')
for g in mydict1:
	num = 0
	for items in mydict1[g]:
		feaid, hypo = items.split('\t\t')[0:2]
		if "hypothetical protein" in hypo:
			num += 1
	f4.write(str(num)+'\t')
f4.write('\n')

f4.write('No hit'+'\t'+'592'+'\n')


f1.close()
f2.close()
f3.close()
f4.close()