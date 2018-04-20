#coding: utf-8
#zhongjie wang
#统计每个subseq对应的bitscore的种类以及每个种类的数量

f1 = open('rhodo5s16s23s.fasta', 'r')
f2 = open('rhodo16s.fasta', 'w')

seqs = f1.read().split('>')

for seq in seqs:
	if 'molecule=16s_rRNA' in seq:
		f2.write('>'+seq)

f1.close()
f2.close()
	
	
