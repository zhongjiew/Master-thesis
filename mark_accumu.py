
f1 = open('3132_exclude_unique_pro_blastp2nr_xml_best_hits.csv','r')
f2 = open('3132_exclude_unique_gene','w')

for line in f1:
	gene = line.split(',')[0]
	if 'Accumulibacter' in line:
		f2.write(gene+'\n')
	else:
		f2.write(gene+'_non-Accumulibacter'+'\n')
