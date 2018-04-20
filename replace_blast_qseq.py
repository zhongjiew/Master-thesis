# -*- coding: utf-8 -*-
###将命名不规则的qseq名称替换成规则的，以方便后面去冗余时提取基因所在的基因组名称

f1 = open("nongi_temp.blastp", "r")
f2 = open('nongi_temp_namelist.txt', 'r')
f3 = open("nongi_temp2.blastp", "w")

infolist = f1.readlines()
namelist = f2.readlines()

for name in namelist:
	name=name.strip('>').strip()
	for info in infolist:
		qseq = info.split('\t')[0]
		other_info = '\t'.join(info.split('\t')[1:])
		if 'gi|' in qseq:
			f3.write(info)
		elif qseq in name:
			f3.write(name+'\t'+other_info)

f1.close()
f2.close()
f3.close()
