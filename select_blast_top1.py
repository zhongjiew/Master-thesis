#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: zhongjie wang ***

f1 = open('rhodocyclales94marker40_filter50.blastp','r')
f2 = open('rhodocyclales94marker40_filter50_top1.blastp', 'w')

corelist = f1.readlines()
#seqlist = f2.read().split('>')

core = []
for line in corelist:
	name = line.split('\t')[0]
	if name not in core:
		core.append(name)

for name in core:
	for line in corelist:
		if name in line:
			f2.write(line)
			break

f1.close()
f2.close()
