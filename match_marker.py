#coding: utf-8
# **author: zhongjie wang**
#在比对到NR筛选后剩下的基因，将其原来比对到的marker基因对应关系提取出来

f1 = open('rhodo94_40marker2nr_blastp_best_hits_rhodocyclalesa_source.csv', 'r')
f2 = open('rhodocyclales94marker40_filter50_top1_relation.tsv', 'r')
f3 = open('rhodo94_40marker2nr_blastp_best_hits_rhodocyclalesa_source_relation.tsv', 'w')

goodlist = f1.readlines()
markerlist = f2.readlines()

for line in markerlist:
	for row in goodlist:
		qseq=row.split(',')[0]
		if qseq in line:
			f3.write(line)

f1.close()
f2.close()
f3.close()
