#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively
# according key words, and then output match numbers


f1 = open(r'I11_match_num.tsv','r')
f2 = open('../2.mcl/out.rhodo.mci.I11', 'r')
f3 = open('type_diff_cluster_num.tsv', 'w')
f4 = open('type_diff_cluster_name.tsv', 'w')

sizelist = f1.readlines()
ortholog_list = f2.readlines()

i = 0
diff_list=[]
for line in sizelist:
	i +=1
	if i ==1:
		f3.write(line)
	else:
		clade1 = list(map(int, line.split('\t')[1:6]))
		clade2 = list(map(int, line.split('\t')[6:11]))
		if all(x for x in clade1) > 0 and sum(clade2)<=0:
			f3.write(line)
			diff_list.append(line)
		elif sum(clade1) == 0 and all(x for x in clade2)>0:
			#print clade1,clade2
			f3.write(line)
			diff_list.append(line)

for ortholog in diff_list:
	n=0
	ortholog_name = ortholog.split('\t')[0]
	for line in ortholog_list:
		n += 1
		ortholog_num = '%04d'%n
		if ortholog_num in ortholog_name:
			f4.write(line)

f1.close()
f2.close()
f3.close()
f4.close()
