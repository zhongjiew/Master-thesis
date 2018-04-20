from collections import defaultdict

f1 = open('accumu5_cov_func.csv','r')
f2 = open('accumu5_info_table.csv', 'w')

lines = f1.readlines()
mydict = defaultdict(dict)
for line in lines:
	genename = line.split(',')[0]
	ortholog = genename.split('_|_')[0]
	genome = genename.split('_|_')[1].split('_')[0]
	if ortholog != 'unique_orthologxxxxx':
		if mydict.get(ortholog):
			mydict[ortholog].append(';'.join([genome]))
		else:
			mydict[ortholog]=[]
			mydict[ortholog].append(';'.join([genome]))


for line in lines:
	coverage1,length=line.split(',')[1:3]
	coverage2=line.split(',')[6]

	genename = line.split(',')[0]
	ortholog = genename.split('_|_')[0]
	section = ortholog.split('_')[0]
	completeness = genename.split(';')[1]
	genome = genename.split('_|_')[1].split('_')[0]
	gc = genename.split('=')[-1]

	reads1=float(coverage1)*float(length)/(150)
	reads2=float(coverage2)*float(length)/(150)
	if 'Bin01.2' in genename:
		reads1_ppm=(reads1/11518411.87)*(1000000)
		reads2_ppm=(reads2/10879981.94)*(1000000)
	if 'Bin02.1' in genename:
		reads1_ppm=(reads1/20784012.26)*(1000000)
		reads2_ppm=(reads2/26829971.96)*(1000000)
	if 'Bin03.6' in genename:
		reads1_ppm=(reads1/2129694.829)*(1000000)
		reads2_ppm=(reads2/3582268.39)*(1000000)
	if 'Bin26.3' in genename:
		reads1_ppm=(reads1/1744239.693)*(1000000)
		reads2_ppm=(reads2/2130117.874)*(1000000)
	if 'Bin31.4' in genename:
		reads1_ppm=(reads1/1667749.425)*(1000000)
		reads2_ppm=(reads2/2065303.65)*(1000000)

	if completeness == 'partial=00':
		complt='Yes'
	else:
		complt='No'
	f2.write(line.strip()+','+section+','+complt+','+gc+','+str(reads1)+','+str(reads2)+','+str(reads1_ppm)+','+str(reads2_ppm)+',')
	if ortholog != 'unique_orthologxxxxx':
		unique_genome=list(set(mydict[ortholog]))
		unique_genome.sort()
		for genome in unique_genome:
			f2.write(genome+';')
		f2.write('\n')
	else:
		f2.write(genome+'\n')


f1.close()
f2.close()
