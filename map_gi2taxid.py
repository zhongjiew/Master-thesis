#coding: utf-8
#zhongjie wang
#20180305
#用法：

import sys

f1 = open('rhodo94_40marker2nr_blastp_best_hits.csv', 'r')
f2 = open('/home/wang/software/ncbi-blast-2.4.0+/gi2taxid.txt', 'r')
f3 = open('lineages-2017-11-15.csv', 'r')
f4 = open('rhodo94_40marker2nr_blastp_best_hits_lineage.csv', 'w')


gilist = f1.readlines()
taxidlist = f2.readlines()
lineagelist = f3.readlines()

lineagedict = {}
for line in taxidlist:
	gi,taxid = line.split('\t')[:2]
	lineagedict[gi] = taxid

for line in gilist:
	gi = line.split(',')[1].split('|')[1]
	for lineage in lineagelist:
		taxid=lineage.split(',')[0]
		if lineagedict[gi]==taxid:
			print taxid
			f4.write(line+','+lineage)
f1.close()
f2.close()
f3.close()
f4.close()
