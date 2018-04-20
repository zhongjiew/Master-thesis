#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words, and then output match numbers #

f1 = open('key.txt', 'r')
f2 = open('out.rhodo.mci.I11', 'r')
f3 = open(r'I11_match_num','w')
keylist = f1.read().split('\t')
orth = f2.readlines()
i = 0
f3.write('keyword\t')
for key in keylist:
		f3.write('%s\t' %key)
f3.write('\n')
for eachline in orth:
		i += 1
		arr = eachline.strip('\n')
		f3.write('ortho%s\t' %i)
		for key in keylist:
			a = arr.count(key)
			if a >= 1:
				a = 1
			f3.write('%d\t' %a)
		f3.write('\n')
f1.close()
f2.close()
f3.close()
