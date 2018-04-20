
#coding:utf-8

#usage：python remove_redundance.py ../2.1.blast2nr/accumu6_incomplete2nr_filter.blastp
#直接输入不完整基因blast比对到NR库的结果

from collections import defaultdict
import sys

mydict=defaultdict(dict)
with open(sys.argv[1],'rt') as fin:
    for line in fin:
        line=line.strip('\n')
        genome,sub=line.split('\t')[0:2]
        sstart,send = line.split('\t')[9:11]
        if genome.startswith('Bin'):
            g=genome.split('_')[0]
        else:
            pass
            #g=genome.split('|')[3][0:4]
        start,end=genome.split('_#_')[1:3]
        length=str(int(end)-int(start)+1)
        if mydict[sub].get(g):
            mydict[sub][g].append('\t\t\t\t'.join([length,line,sstart,send]))
        else:
            mydict[sub][g]=[]
            mydict[sub][g].append('\t\t\t\t'.join([length,line,sstart,send]))

wfout=open('want.txt','wt')
afout=open('all.txt','wt')
f4=open('query_unique.txt', 'w')

all_query=[]
for sub in mydict:
    for g in mydict[sub]:
        max_len,max_line,start,end=mydict[sub][g][0].split('\t\t\t\t')
        all_query.append(max_line.split('\t')[0])
        for content in mydict[sub][g]:
            l1,l2,s3,e4=content.split('\t\t\t\t')
            afout.write(sub+'\t'+l2+'\n')
            if int(s3) >= int(end) or int(start) >= int(e4):
            	if int(l1)>int(max_len):
                	max_line=l2
        wfout.write(sub+'\t'+max_line+'\n')

unique_query = set(all_query)
for a in unique_query:
	f4.write(a+'\n')