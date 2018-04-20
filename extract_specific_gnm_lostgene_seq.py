#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output core cluster in which specific genome is absent#
import re

for i in range(1, 11):
	f1 = open("cluster_name/genome%s_lost_cluster_name"%i, "r")
	f2 = open('../../accumu10_orf_nuc.fasta', 'r')
	f3 = open("cluster_seq/specific_genome%s_lost_gene.fasta"%i, "w")


	accumulist = []

	for line in f1:
		s = re.search('(UW-1.*)', line)
		if s:
			uw = s.group(1).split('\t')[0]
			accumulist.append(uw)
		else:
			accumulist.append(line.split()[0])
	seqs = f2.read()
	seq_list = seqs.split('>')
	for seq in seq_list:
		genename = seq.split('\n')[0].split(' # ')[0]
		for a in accumulist:
			if a == genename:
				f3.write('>'+seq)

		
	f1.close()
	f2.close()
	f3.close()
