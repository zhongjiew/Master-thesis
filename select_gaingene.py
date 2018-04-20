#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***
# 提取出一个节点的gain gene:现根据节点A和其祖先节点B的core gene，coreA-coreB则认为是节点A的gain gene。

f1 = open('clade1_coregene_name_list', 'r')
f2 = open('accumu8.coregene_name_list', 'r')
f3 = open('clade1orf.pro.fasta', 'r')
f4 = open('clade1_gain_gene_name_list', 'w')
f5 = open('clade1_gain_gene_seq_pro.fasta', 'w')

Alist = f1.read().split('\n')
Blist = f2.read().split('\n')
accumulist = []

#生成gain gene的list
for Agene in Alist:
		if Agene not in Blist:
			accumulist.append(Agene)

#将gain gene写出文件
for a in accumulist:
	f4.write(a+'\n')

#根据gain gene list抽出所有的序列
seq_list = f3.read().split('>')
for a in accumulist:
	for seq in seq_list:
		if a in seq:
			f5.write('>'+seq)
	
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
