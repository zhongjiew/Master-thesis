#zhongjie wang
#2018/1/26

from collections import defaultdict
import re

f1 = open('q00000.keg', 'r')
f2 = open('accumu5_cov_func.txt', 'r')
f3 = open('kegg_pathway_rpkm1_gcov_sum.txt', 'w')
f4 = open('kegg_pathway_rpkm2_gcov_sum.txt', 'w')

Apart = f1.read().split('A09')[1:]
rpkmlist = f2.readlines()

dicB1 = defaultdict(list)
dicB2 = defaultdict(list)
rpkm_dict = defaultdict(list)

for line in rpkmlist:
	genename = line.split('\t')[0]
	rpkm1_gcov = line.split('\t')[5]
	rpkm2_gcov = line.split('\t')[10]
	rpkm_dict[genename].append(rpkm1_gcov)
	rpkm_dict[genename].append(rpkm2_gcov)

B = ''
for part in Apart:
	Bpart = part.split('\n')
	A = Bpart[0]
	f3.write('A09'+A)
	f4.write('A09'+A)
	dicB1 = defaultdict(list)
	dicB2 = defaultdict(list)
	for line in Bpart[1:]:
		#sum1, sum2 = 0, 0
		if re.match('B  ',line):
			B=line.strip()
		elif 'D      ' in line:
			for genename in rpkm_dict:
				if genename in line:
					rpkm1_gcov, rpkm2_gcov= rpkm_dict[genename][:]
					dicB1[B].append(float(rpkm1_gcov))
					dicB2[B].append(float(rpkm2_gcov))	

	for B in dicB1:
		sum1 = sum(dicB1[B])
		f3.write('\t'+B+'\t'+str(sum1)+'\n') 
	for B in dicB2:
		sum2 = sum(dicB2[B])
		f4.write('\t'+B+'\t'+str(sum2)+'\n')


f1.close()
f2.close()
f3.close()
f4.close()