# -*- coding: utf-8 -*-
### resort blastp result ###

file1 = open("accumu21.good.blastp", "r")
file2 = open("core_cluster.txt", "w+")

corelist = file1.readlines()
a = []

for genes in corelist:
	core = genes.split('\t')[0]
	if core not in a:
		a.append(core)

for key in a:
	for genes in corelist:
		name = genes.split('\t')
		if key == name[0]:
			file2.write(name[1]+'\t')
	file2.write('\n')

file1.close()
file2.close()
