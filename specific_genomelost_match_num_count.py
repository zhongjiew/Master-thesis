#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output core cluster in which specific genome lost gene#

f1 = open("core_cluster_match_num", 'r')
f3 = open("match_num_count", "w")

numlist = f1.readlines()

for i in range(1, 11):
	#f2 = open("specific_genome%s_lost_cluster"%i, "a")
	a, b = 0, 0
	for line in numlist:
		a += 1
		num = line.split('\t')
		if a == 1:
			#f2 = open("%s_lost_cluster"%num[i], "a")
			f3.write("%s"%num[i]+'\t')
		else:
			if int(num[i]) == 0:
				b += 1
				#f2.write(line)
	f3.write(str(b)+'\n')
f3.write("All"+'\t'+str(a-1))

f1.close()
f3.close()