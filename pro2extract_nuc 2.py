
f1 = open('unique/1.2.3.26_unique_pro.fasta','r')
f2 = open('1.2.3.26_orf_nuc_good.fasta', 'r')
f3 = open('1.2.3.26_unique_nuc.fasta', 'w')

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
