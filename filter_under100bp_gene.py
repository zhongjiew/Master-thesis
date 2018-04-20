# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("accumu10_orf_pro.fasta", "r")
fileout = open("accumu10_orf_pro_good.fasta", "w")

genelist = file_in.readlines()
dic, k, v = {}, '', []

for i in genelist:
	if i.startswith('>'): 
		dic[k] = v 
		k = i[1:-1] 
		v = []
	else:
		v.append(i)
dic[k] = v
dic.pop('')
print("sequences in total: %s" %len(dic))

for (k, v) in dic.items():
	seq = ''.join(v)
	#genelen = sum(map(len, v))
	genelen = len(seq)
	if genelen > 50:
		fileout.write(">"+k+'\n'+seq)
file_in.close()
fileout.close()
