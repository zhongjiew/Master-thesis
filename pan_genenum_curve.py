#! /usr/bin/env python 
#! -*- coding: utf-8 -*-
# Author: zhongjie wang

import random

f1 = open('proteinsnum', 'r')
f2 = open('accmulate_num', 'w')

numberlist = f1.read().split(',')
accmulatelist = []

for n in range(1, 41)
	for i in range(1, 101):
		randomlist = random.sample(numberlist, '%s'%n)
		a = 0
		for num in randomlist:
			a += int(num)
			f2.write(str(a)+'\t')
		f2.write('\n')

f1.close()
f2.close()