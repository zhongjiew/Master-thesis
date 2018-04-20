from collections import defaultdict

f1 = open('accumu5_cov_func.csv','r')
f2 = open('accumu5_info_table.csv', 'w')

lines = f1.readlines()
mydict = defaultdict(dict)
for line in lines:
	genename = line.split(',')[0]
	ortholog = genename.split('_|_')[0]
	genome = genename.split('_|_')[1].split('_')[0]
	if mydict.get(ortholog):
		if genome not in mydict[ortholog].values():
			mydict[ortholog].append(genome)
	else:
		mydict[ortholog]=[]
		mydict[ortholog]=genome


for line in lines:
	genename = line.split(',')[0]
	ortholog = genename.split('_|_')[0]
	section = ortholog.split('_')[0]
	completeness = genename.split(';')[1]
	gc = genename.split('=')[-1]
	if completeness == 'partial=00':
		complt='Yes'
	else:
		complt='No'
	f2.write(line.strip()+','+section+','+complt+','+gc+',')
	for genome in mydict[ortholog]:
		f2.write(genome+';')
	f2.write('\n')


f1.close()
f2.close()
