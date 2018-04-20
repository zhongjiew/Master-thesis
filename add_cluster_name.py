#! /usr/bin/env python
# -*- coding: utf-8 -*-
# adding 4 cluster category name(core,major,rare,unique) to each gene name according which cluster it belongs to.

f1 = open('../mcl/out.rhodo.mci.I11', 'r')
f2 = open('../../clade10_orf_pro.fasta', 'r')
f3 = open('../../clade10_orf_nuc.fasta', 'r')
f4 = open('clade10_orf_pro_add_cluster.fasta', 'w')
f5 = open('clade10_orf_nuc_add_cluster.fasta', 'w')

ortholog = f1.readlines()
prolist = f2.read().split('>')
nuclist = f3.read().split('>')
keylist = []
#clusterlist = {core, major, rare, unique}

for eachline in ortholog:
	genes = eachline.split('\t')
	for gene in genes:
		if "gi|" in gene:
			keyword = gene.split('|')[3][:6]
		else:
			keyword = gene.split('_')[0]
			
		if keyword not in keylist:
			keylist.append(keyword)

	num = len(keylist)
	if num <= 1:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f4.write('>unique_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f5.write('>unique_'+nuc)
			#clusterlist[unique].append('\t\t'.join(gene))
	if num >= 2 and num <= 3:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f4.write('>rare_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f5.write('>rare_'+nuc)
	if num >= 4 and num <= 6:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f4.write('>major_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f5.write('>major_'+nuc)
	if num >= 7:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f4.write('>core_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f5.write('>core_'+nuc)
	keylist = []

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
