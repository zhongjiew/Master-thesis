#! usr/bin/env/ python
# -*- coding: utf-8 -*-
#Author: zhongjie wang
# input genome completeness must be decimal, seperated by tab(\t).
#生成的core_genome_cutoff_pattern是非常详细的每种可能性的结果
#生成的core_genome_cutoff_sum是缺失基因数增加时，能够覆盖所有基因的概率值的累积和，最终的cutoff看这个文件就可以了

from random import sample
from operator import mul
from scipy.special import comb, perm
from itertools import combinations, permutations

f1 = open("genome_completeness", 'r')
f2 = open('core_genome_cutoff_pattern.txt', 'w')
f3 = open('core_genome_cutoff_sum.txt', 'w')

orilist = f1.read().split('\t')

# generate presence list; a is original list ;b is absence list.
def presence(a, b):
	clist = []
	for i in a:
		if i in b:
			b.remove(i)
		else:
			clist.append(i)
	return clist

 # generate the product of presence list
def production1(alist):
	p = 1
	for a in alist:
		p *= float(a)
	return p

 # generate the product of absence list
def production2(blist):
	p = 1
	for b in blist:
		p *= (1-float(b))
	return p

# recursively generate products of a list
def fib(dlist):
	dsum = 0
	for d in dlist:
		dsum += float(d)
		return dsum

# generate the products of all present pattern 
f3.write('0 absent gennomes:'+'\t'+str(production1(orilist))+'\n')

# append the final results of different absent genomes to list.
result = []
result.append(str(production1(orilist)))

for i in range(1, 11):
	# all combinations of absent patterns 
	asum = 0
	absencelists = list(combinations(orilist, i))
	for absencelist in absencelists:
		presencelist = presence(orilist, list(absencelist))
		production = production1(presencelist)*production2(absencelist)

		f2.write(str(production)+'\t')
		asum += production
	f2.write('\n')
	result.append(asum)
	f3.write('%s absent gennomes:'%i+'\t'+str(asum)+'\n')

dsum = 0
for d in result:
	dsum += float(d)
	f3.write("recursive sum: %.4f"%dsum+'\t')

f1.close()
f2.close()
f3.close()
