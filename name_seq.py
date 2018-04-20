#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 
f1 = open("细菌生长相关基因列表.csv", "r")
f2 = open("细菌生长相关基因.fasta", "w")

for line in f1:
	name1 = line.split(",")[0]
	name2 = line.split(",")[7]
	seq = line.split(",")[8]
	f2.write(">"+name1+"_operon_"+name2+"\n"+seq)

f1.close()
f2.close()
