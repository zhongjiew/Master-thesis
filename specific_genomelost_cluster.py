#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output core cluster in which specific genome is absent#

f1 = open("../core_cluster_match_num", 'r')

numlist = f1.readlines()

for i in range(1, 11):
	f2 = open("specific_genome%s_lost_cluster"%i, "a")
	a, b = 0, 0
	for line in numlist:
		a += 1
		num = line.split('\t')
		if a == 1:
			#f2 = open("%s_lost_cluster"%num[i], "a")
			f2.write(line)
		else:
			if int(num[i]) == 0:
				f2.write(line)
f1.close()
f2.close()
