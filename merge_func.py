f1 = open('../accumu5_two_metatrans_cov.csv', 'r')
f2 = open('accumu6_nuc2nr_best_hits.csv', 'r')
f3 = open('accumu5_cov_func.csv','w')

lines1 = f1.readlines()
lines2 = f2.readlines()

dict2 = {}
for line2 in lines2:
	line2 = line2.strip()
	name2 = line2.split(',')[0]
	func = line2.split(',')[-1]
	dict2[name2] = func

for line1 in lines1:
	line1 = line1.strip()
	name1 = line1.split(',')[0]
	if name1 in dict2:
		f3.write(line1+','+dict2[name1]+'\n')
	else:
		f3.write(line1+'\n')

f1.close()
f2.close()
f3.close()
