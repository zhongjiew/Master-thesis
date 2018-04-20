#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

### extract orthologous gene cluster into files ###

f1 = open('pan_single_copy.I11', 'r')
f2 = open('all42orf.fasta', 'r')
f3 = open('key.txt', 'r')
#orths = f1.readlines()
genes = f2.read().split('>')
keyword = f3.read().split('\t')

i = 1
cluster_keylist = []
cluster_ortholog = ''

for orthlines in f1:
	orths = orthlines.strip().split('\t')
	for orth in orths:
		cluster_keylist.append(orth[:5])

	for key in keyword:
		if key not in cluster_keylist:
			cluster_ortholog += '>'+key+'\n'
		else:
			for orth in orths:
				for gene in genes:
					if orth in gene:
						cluster_ortholog += '>'+gene+'\n'
			
	for key in keyword:
		orthologs = cluster_ortholog.split(">")
		for ortholog in orthologs:
			if key in ortholog:
				f4 = open('single_copy_ortholog%s.fasta' %str(i), 'w')
				f4.write('>'+ortholog)
				f4.close()

				
	cluster_keylist = []
	cluster_ortholog = ''

	i += 1
	if i > 10:		#the number of orthologous clusters.
		break
f1.close()
f2.close()
f3.close()
