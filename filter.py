# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("rhodoblastp-rename2", "r")
fileout = open("rhodoblastpfilter", "w+")

for num in file_in:
	i = num.split('\t')
	if float(i[2]) >= 70.00 and float(i[3]) >=75.00:
		fileout.write(num)
file_in.cloce()
fileout.cloce()
