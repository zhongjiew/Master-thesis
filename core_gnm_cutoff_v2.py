#! usr/bin/env/ python
# -*- coding: utf-8 -*-
#Author: zhongjie wang
#input genome completeness must be decimal (0.****), seperated by tab(\t).
#生成的core_genome_cutoff_sum.txt是随着基因组缺失容忍度的增加，能够包含核心基因的比例逐渐增加为多少
#这个版本Version2适用于基因组数量比较多(不低于20个)时，随机取样求平均值，会节省大量的计算时间

from random import sample
import numpy as np
from operator import mul
#from scipy.special import comb, perm
from itertools import combinations, permutations

f1 = open("completeness.txt", 'r')
f2 = open('core_genome_cutoff_sum2.txt', 'w')

origin_list = f1.read().split('\t')

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
def product1(alist):
	p = 1
	for a in alist:
		p *= float(a)
	return p

 # generate the product of absence list
def product2(blist):
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
#f3.write('0 gennome absent:'+str(product1(orilist))+'\t')
#f3.write("when 0 gennomes' absent: containing gene percentage:%.4f"%(product1(orilist))+'\n')

#i为循环的次数，50次;随机取20个基因组,最好不要超过20个，不然计算量会大很多。
cycle = 50
sample_genome = 25

#生成一个都是0的一维数组，用数组是因为数组可以直接用于运算
final_result=np.zeros(sample_genome+1)

for i in range(1, cycle+1):
	print 'No.%d cycle'%i
	#随机从所有的基因组完整度list中抽取20个
	test_list = sample(origin_list, sample_genome)
	result = []
	result.append(product1(test_list))
	#计算从0到20个基因组缺失的情况下的结果
	for m in range(1, len(test_list)+1):
	# all combinations of absent patterns 
		asum = 0
		absencelists = list(combinations(test_list, m))
		for absencelist in absencelists:
			presencelist = presence(test_list, list(absencelist))
			product = product1(presencelist)*product2(absencelist)
			asum += product
		print asum	
		result.append(asum)
	#将每个循环的结果相加，以方便后面求平均值
	final_result = final_result+np.array(result)

#get average result
final_result = final_result/cycle

#输出最终结果
dsum,n = 0,-1
for d in final_result:
	n+=1
	dsum += float(d)
	f2.write("when %d gennomes' absent: containing gene percentage:%.4f"%(n,dsum)+'\n')

f1.close()
f2.close()
