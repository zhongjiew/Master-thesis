
f1 = open('3132_exclude_unique_marked_gene','r')
f2 = open('31.32_orf_nuc_good.fasta', 'r')
f3 = open('31.32_exclude_unique_orf_nuc_marked_gene.fasta','w')

namelist = f1.readlines()
prolist = f2.read().split('>')

for name in namelist:
	for pro in prolist:
		pro_name = pro.split('\n')[0]
		seq = '\n'.join(pro.split('\n')[1:])
		if pro_name in name and seq.strip() != '':
			f3.write('>'+name+seq)
			break

f1.close()
f2.close()
f3.close()
