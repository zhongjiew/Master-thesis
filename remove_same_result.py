#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Athour: zhongjie wang

f1 = open('incomplete.filter.blastp', 'r')
f2 = open('incomplete.filter_map_uniq.blastp', 'w')

maplist = f1.read().split('\n')
uniqlist = set(maplist)

for line in uniqlist:
	f2.write(line+'\n')

f1.close()
f2.close()
