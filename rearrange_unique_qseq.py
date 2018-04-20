#coding: utf-8
# **author: zhongjie wang**
#对unique后的marker基因blast结果，按照每行一个基因组，每列一个marker的格式进行重排
#用法：python rearrange_unique_qseq.py unique_relation.tsv rearrange_qseq.tsv rearrange_num.tsv  final_good_qseq.txt

import sys
from collections import defaultdict

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')
f3 = open(sys.argv[3], 'w')
f4 = open(sys.argv[4], 'w')

hitlist=f1.readlines()

binlist,markerlist=[],[]
mydict = defaultdict(dict)
for hit in hitlist:
	qseq,marker,piden=hit.split('\t')[:3]
	if 'gi|' in qseq:
		genome=qseq.split('_')[0].split('|')[-2][:4]
		if mydict[marker].get(genome):
			mydict[marker][genome].append(';;;'.join([qseq,piden]))
		else:
			mydict[marker][genome]=[]
			mydict[marker][genome].append(';;;'.join([qseq,piden]))
		if genome not in binlist:
			binlist.append(genome)

	else:
		genome=qseq.split('_')[0]
		if mydict[marker].get(genome):
			mydict[marker][genome].append(';;;'.join([qseq,piden]))
		else:
			mydict[marker][genome]=[]
			mydict[marker][genome].append(';;;'.join([qseq,piden]))
		if genome not in binlist:
			binlist.append(genome)
	
	if marker not in markerlist:
		markerlist.append(marker)

markerlist.sort()
for marker in markerlist:
	f2.write('\t'+marker)
	f3.write('\t'+marker)
f2.write('\n')
f3.write('\n')

for genome in binlist:
	print genome
	f2.write(genome+'\t')
	f3.write(genome+'\t')
	for marker in markerlist:
		if genome in mydict[marker]:
			num=len(mydict[marker][genome])
			seqs=mydict[marker][genome]
			for seq in seqs:
				qseq=seq.split(';;;')[0]
				f2.write(str(seq)+',')
			f2.write('\t')
			f3.write(str(num)+'\t')
		else:
			f2.write('\t')
			f3.write('0\t')

	f2.write('\n')
	f3.write('\n')


for marker in mydict:
	for genome in mydict[marker]:
		num=len(mydict[marker][genome])
		seqs=mydict[marker][genome]
		max_qseq,max_piden=mydict[marker][genome][0].split(';;;')[:]
		if num>1:
			for seq in seqs:
				qseq,piden=seq.split(';;;')[:]
				if float(piden)>float(max_piden):
					max_piden,max_qseq=piden,qseq
			f4.write(max_qseq+'\t'+marker+'\n')

		else:
			f4.write(max_qseq+'\t'+marker+'\n')


f1.close()
f2.close()
f3.close()

