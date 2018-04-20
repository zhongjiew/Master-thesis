# -*- coding: utf-8 -*-
### filter blastp result ###

file_in = open("10clade.blastp", "r")
fileout = open("10clade_60%_filter.blastp", "w+")

for num in file_in:
	i = num.split('\t')
	if float(i[2]) >= 60.00 and float(i[3]) >=75.00:
		fileout.write(num)
file_in.close()
fileout.close()
