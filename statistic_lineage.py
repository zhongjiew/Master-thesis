#!usr/bin/python
#coding: utf-8
#统计种系信息：届门纲目科属种各为一列，统计每一列中的种类和数目

f1 = open('top10_subject_description_rename_megan_out.csv', 'r')
f2 = open("top10_megan_out_lineage_statistic.csv", "w")

lines = f1.readlines()

for i in range(3, 11):
	lineage_num = []
	lineage_kind = []
	for line in lines:
		#print line
		lineage = line.split(',')[i]
		print i
		print lineage
		lineage_num.append(lineage)
		if lineage not in lineage_kind:
			lineage_kind.append(lineage)

	for lineage in lineage_kind:
		num = 	lineage_num.count(lineage)
		f2.write(lineage+'\t'+str(num)+',')
	f2.write('\n')
f1.close()
f2.close()
