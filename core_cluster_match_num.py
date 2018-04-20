#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output core cluster match numbers #

f1 = open("I11_match_num", 'r')
f2 = open("core_cluster_match_num", "w")

numlist = f1.readlines()
a = 0

for line in numlist:
	a += 1
	if a == 1:
		f2.write(line)
	else:
		num = line.split('\t')
		result = 0
		for i in range(1, 11):
			result += int(num[i])
		if result > 8:
			f2.write(line)
			
f1.close()
f2.close()