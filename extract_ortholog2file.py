#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

### extract orthologous gene cluster into files ###

f1 = open('../type_diff_cluster_name.tsv', 'r')
f2 = open('../../3.add_cluster_name/clade10_orf_add_cluster.faa', 'r')

orths = f1.readlines()
fasta = f2.read().split('>')
i = 1

for orthline in orths:
    orthline = orthline.strip().split('\t')
    for orth in orthline:
        for gene in fasta:
            if orth in gene:
                f3 = open('ortholog%s.fasta' %str(i), 'a')
                f3.write('>'+'%s\n' %gene)
                f3.close()
    i += 1
    if(i>116):
        break
f1.close()
f2.close()
