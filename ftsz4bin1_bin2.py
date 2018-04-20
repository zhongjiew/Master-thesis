#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: zhongjie wang ***

import sys
f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')

genelist = f1.readlines()

orthlist = []
for line in genelist:
	ortholog = line.split(',')[0].split('_|_')[0]
	if ortholog not in orthlist and 'unique_ortholog' not in ortholog:
		orthlist.append(ortholog)

orthlist1 = []
for ortholog in orthlist:
	for line in genelist:
		if ortholog in line:
			norm_rpkm1 = line.split(',')[5]
			norm_rpkm2 = line.split(',')[-1]
		 	if 'Bin01.2' in line:
				if float(norm_rpkm1) > 0.01603 or float(norm_rpkm2) > 0.010572493:
		 			if float(norm_rpkm1) / float(norm_rpkm2) > 1.5 and ortholog not in orthlist1:
		 				orthlist1.append(ortholog)

good_orthlist = []
for ortholog in orthlist1:
	for line in genelist:
		if ortholog in line:
			norm_rpkm1 = line.split(',')[5]
			norm_rpkm2 = line.split(',')[-1]
			if 'Bin02.1' in line:
	 			if float(norm_rpkm1) > 0.013841446 or float(norm_rpkm2) > 0.013755867:
					if float(norm_rpkm1) / float(norm_rpkm2) <= 0.66 and ortholog not in good_orthlist:
						good_orthlist.append(ortholog)
print len(good_orthlist)
for line in genelist:
	for ortholog in good_orthlist:
		if ortholog in line:
			norm_rpkm1 = line.split(',')[5]
			norm_rpkm2 = line.split(',')[-1]
			if 'Bin01.2' in line:
				if float(norm_rpkm1) > 0.01603 or float(norm_rpkm2) > 0.010572493:
		 			if float(norm_rpkm1) / float(norm_rpkm2) > 1.5:
		 				f2.write(line)
	 		elif 'Bin02.1' in line:
	 			if float(norm_rpkm1) > 0.013841446 or float(norm_rpkm2) > 0.013755867:
					if float(norm_rpkm1) / float(norm_rpkm2) <= 0.66: 
						f2.write(line)

f1.close()
f2.close()
