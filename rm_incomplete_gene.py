#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

f1 = open('rhodocylales93.fna', 'r')
f2 = open('rhodocylales93_orf_complete.fna', 'w')

genes = f1.read().split('>')

for gene in genes:
	if 'partial=00' in gene:
		f2.write('>'+gene)
	
f1.close()
f2.close()