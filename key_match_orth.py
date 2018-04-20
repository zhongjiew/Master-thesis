#! /usr/bin/env python
# this script aims to match orthologous gene clusters to all genomic titles respectively #
# according key words， and then output match numbers #

f1 = open('key.txt', 'r')
f2 = open(out.rhodo.mci.I15', 'r')
f3 = open(r'outI15','w')
keylist = f1.read().split('\t')
orth = f2.readlines()
for eachline in orth:
    arr = eachline.strip('\n')
    for key in keylist:
        a = arr.count(key)
        f3.write('%s\t%d\t'%(key,a))
    f3.write('\n')
f1.close()
f2.close()
f3.close()
