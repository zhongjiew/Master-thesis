# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("31.32.blastp", "r")
fileout = open("31.32_psc_70%_filter.blastp", "w+")

for num in file_in:
	i = num.split('\t')
	if float(i[2]) >= 70.00 and float(i[3]) >=75.00:
		fileout.write(num)
file_in.close()
fileout.close()
