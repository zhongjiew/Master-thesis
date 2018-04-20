#zhongjie wang
#2017/10/19
#extract nuc sequence according to pro seq name

f1 = open('accumu19_pro_good.faa','r')
f2 = open('accumu19_nuc.fna', 'r')
f3 = open('accumu19_nuc_good.fasta', 'w')

prolist = f1.read().split('>')
nuclist = f2.read().split('>')

for pro in prolist:
	pro_name = pro.split('\n')[0]
	for nuc in nuclist:
		nuc_name = nuc.split('\n')[0]
		seq = '\n'.join(nuc.split('\n')[1:])
		if nuc_name in pro and seq.strip() != '':
			f3.write('>'+pro_name+'\n'+seq)
			break

f1.close()
f2.close()
f3.close()
