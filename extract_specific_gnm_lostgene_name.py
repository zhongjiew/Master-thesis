#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output core cluster in which specific genome is absent#

f1 = open("../out.rhodo.mci.I11", 'r')

clusters = f1.readlines()

for i in range(1, 11):
	f2 = open("cluster_matchnum/specific_genome%s_lost_cluster"%i, "r")
	f3 = open("cluster_name/genome%s_lost_cluster_name"%i, "w")
	lines = f2.read().split('\n')

	rowlist = []
	m = 0
	for key in lines:
		m += 1
		num = key.split('\t')[0][5:]
		if m == 1:
			continue
		else: 
			print num
			a = 0
			for line in clusters:
				a += 1
				if str(a) == num:
					f3.write(line)

f1.close()
f2.close()
f3.close()
