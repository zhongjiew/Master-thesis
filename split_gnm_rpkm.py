#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: zhongjie wang ***
#

f1 = open('two_metatrans_rpkm.csv','r')
f2 = open('rpkm/metatrans1_pansc.csv', 'w')
f3 = open('rpkm/metatrans2_pansc.csv','w')
f4 = open('rpkm/radio_meta1_meta2.csv', 'w')

psclist = f1.readlines()

gnm = []
for line in psclist:
	print line
	gnm_name = line.split('_|_')[1][:7]
	if gnm_name not in gnm:
		gnm.append(gnm_name)

for gnm_name in gnm:
	f2.write(gnm_name+',')
	f3.write(gnm_name+',')
	f4.write(gnm_name+',')
	for line in psclist:
		print line
		meta1 = line.split(',')[1]
		meta2 = line.split(',')[2]
		radio = line.split(',')[3].strip()
		if gnm_name in line:
			f2.write(meta1+',')
			f3.write(meta2+',')
			f4.write(radio+',')
	f2.write('\n')
	f3.write('\n')
	f4.write('\n')


f1.close()
f2.close()
f3.close()
f4.close()
