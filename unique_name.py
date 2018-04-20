#! /usr/bin/env python
# -*- coding: utf-8 -*-

f1 = open('seqname.csv', 'r')
f2 = open('unique_seqname.csv', 'w')

alist = []

#生成gain gene的list
for name in f1:
		if name not in alist:
			alist.append(name)

#将gain gene写出文件
for a in alist:
	f2.write(a)

f1.close()
f2.close()