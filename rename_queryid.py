#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

f1 = open('top10_subject_description_out.csv', 'r')
f2 = open('top10_subject_description_rename.csv', 'w')

allquerylist = f1.readlines()
i = 1

for allqueryids in allquerylist:
	allquery = allqueryids.split(',')[0]
	new_query = allquery+'_'+str(i)
	i += 1
	f2.write(new_query+','+allqueryids)

f1.close()
f2.close()
