#! /usr/bin/env python
# -*- coding: utf-8 -*-
# adding 4 cluster category name(core,major,rare,unique) to each gene name according which cluster it belongs to.

f1 = open('../mcl/out.rhodo.mci.I11', 'r')
f2 = open('../../clade10_orf_pro.fasta', 'r')
f3 = open('../../clade10_orf_nuc.fasta', 'r')
f41 = open('clade10_orf_pro_unique_add_cluster.fasta', 'w')
f42 = open('clade10_orf_pro_minus_add_cluster.fasta', 'w')
f43 = open('clade10_orf_pro_major_add_cluster.fasta', 'w')
f44 = open('clade10_orf_pro_core_add_cluster.fasta', 'w')
f51 = open('clade10_orf_nuc_unique_add_cluster.fasta', 'w')
f52 = open('clade10_orf_nuc_minus_add_cluster.fasta', 'w')
f53 = open('clade10_orf_nuc_major_add_cluster.fasta', 'w')
f54 = open('clade10_orf_nuc_core_add_cluster.fasta', 'w')

ortholog = f1.readlines()
prolist = f2.read().split('>')
nuclist = f3.read().split('>')
keylist = []
n = 0
#clusterlist = {core, major, rare, unique}

for eachline in ortholog:
	n += 1
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
					f41.write('>unique_'+'ortholog'+str('%05d'%n)+'_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f51.write('>unique_'+'ortholog'+str('%05d'%n)+'_'+nuc)
	if num >= 2 and num <= 3:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f42.write('>minus_'+'ortholog'+str('%05d'%n)+'_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f52.write('>minus_'+'ortholog'+str('%05d'%n)+'_'+nuc)
	if num >= 4 and num <= 6:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f43.write('>major_'+'ortholog'+str('%05d'%n)+'_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f53.write('>major_'+'ortholog'+str('%05d'%n)+'_'+nuc)
	if num >= 7:
		for gene in genes:
			for pro in prolist:
				if gene in pro:
					f44.write('>core_'+'ortholog'+str('%05d'%n)+'_'+pro)
			for nuc in nuclist:
				if gene in nuc:
					f54.write('>core_'+'ortholog'+str('%05d'%n)+'_'+nuc)
	keylist = []

f1.close()
f2.close()
f3.close()
f41.close()
f42.close()
f43.close()
f44.close()
f51.close()
f52.close()
f53.close()
f54.close()