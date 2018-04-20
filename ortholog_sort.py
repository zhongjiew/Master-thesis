#！ /usr/bin/env python

### this script aims to extract orthologous gene cluster names according to match result key_match_orth.py genetated. ###


i = 0
for i in range(1, 50):
	f1 = open('key.txt', 'r')
	f2 = open('ortholog%s.fasta'%i, 'r')
	
	keylist = f1.read().split('\t')
	genelist = f2.read().split('>')

	for key in keylist:
		for gene in genelist:
			if key in gene:
				f3 = open('ortholog_sorted%s'%i,'a+')
				f3.write('>'+gene)
		
f1.close()
f2.close()
f3.close()