#zhongjie wang

import numpy as np
import pandas as pd

f1 = open('20nodes_clade.tsv', 'r')
f2 = open('20nodes_clade_binary.tsv', 'w')

mydata = f1.readline()

for line in mydata:
	#print line
	if line.strip() > 1:
		line == 1
		f2.write(line)
	else:
		f2.write(line)


	

f1.close()
f2.close()