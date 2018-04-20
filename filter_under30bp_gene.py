# -*- coding: utf-8 -*-
### filter gene length ###

f1 = open("accumu19_pro_incomplete.fasta", "r")
f2 = open("accumu19_pro_incomplete_abv30bp.fasta", "w")

genelist = f1.read().split('>')

for gene in genelist:
	name = gene.split('\n')[0]
	seq = ''.join(gene.split('\n')[1:])
	if len(seq) >= 30:
		f2.write('>'+gene)

f1.close()
f2.close()
