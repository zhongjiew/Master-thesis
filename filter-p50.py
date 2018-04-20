# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("1.2.3.26.blastp", "r")
fileout = open("1.2.3.26_psc_50%_filter.blastp", "w+")

for num in file_in:
	i = num.split('\t')
	if float(i[2]) >= 50.00 and float(i[3]) >=75.00:
		fileout.write(num)
file_in.close()
fileout.close()
