f1 = open('metatrans1_cov_length2.csv', 'r')
f2 = open('metatrans2_cov_length2.csv','r')
f3 = open('../accumu6_nuc_add_cluster.fasta', 'r')
f4 = open('two_metatrans_cov.csv','w')

lines1 = f1.readlines()
lines2 = f2.readlines()
genename = []

for line in f3:
	if line.startswith('>'):
		name = line[1:]
		if name not in genename:
			genename.append(name.strip())
dict1 = {}
for line1 in lines1:
	line1 = line1.strip()
	name1 = line1.split(',')[0]
	info1 = ','.join(line1.split(',')[1:])
	dict1[name1] = info1
	
dict2 = {}
for line2 in lines2:
	line2 = line2.strip()
	name2 = line2.split(',')[0]
	info2 = ','.join(line2.split(',')[1:])
	dict2[name2] = info2
	
for name in genename:
	if name in dict1.keys() and name in dict2.keys():
		f4.write(name+','+dict1[name]+','+dict2[name]+'\n')
	elif name in dict1.keys() and name not in dict2.keys():
		f4.write(name+','+dict1[name]+6*',0'+'\n')
	elif name not in dict1.keys() and name in dict2.keys():
		f4.write(name+6*',0'+dict2[name]+'\n')
	else:
		f4.write(name+10*',0'+'\n')

f1.close()
f2.close()
f3.close()
