# -*- coding: utf-8 -*-
### caculate average aa length of every orthologous gene cluster ###
### first count all aa base number, then caculate average sequence number ###

filein = open('ortholog40.fasta', 'r')
 
dic, k, v = {}, '', []
 
for i in filein:
    if i.startswith('>'): 
        dic[k] = v 
        k = i[1:-1] 
        v = []
    else:
        v.append(i)
dic[k] = v
dic.pop('')
print("sequences in total: %s" %len(dic))

a=len(dic)
b=0
for (k, v) in dic.items():
    print("SEQUENCE: %s\nLENGTH:%s" %(k, sum(map(len, v))))
    b = b + int(sum(map(len,v)))
average = int(b/a)
print("average sequence length: %s" %average)
filein.close()
