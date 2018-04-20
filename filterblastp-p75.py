# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("rhodoblastpout", "r")
fileout = open("rhodoblastpfilter-p75", "w+")

for num in file_in:
	i = num.split('\t')
	if float(i[2]) >= 70.00 and float(i[3]) >=75.00:
		fileout.write(num)
file_in.close()
fileout.close()
