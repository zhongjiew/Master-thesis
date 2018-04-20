#zhongjie wang


f1 = open('keylist.txt', 'r')
f2 = open('keylist_num.txt', 'w')

ortholog = f1.readlines()
keylist = []
print ortholog

for keyword in ortholog:
	if keyword not in keylist:
		print keyword
		keylist.append(keyword)

for key in keylist:
	num = ortholog.count(key)
	f2.write(key.strip()+'\t'+str(num)+'\n')

f1.close()
f2.close()