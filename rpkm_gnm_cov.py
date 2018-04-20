f1 = open('metatrans1_cov_length.csv','r')
f2 = open('metatrans2_cov_length.csv','r')
f3 = open('metatrans/metatrans1_cov_length2.csv', 'w')
f4 = open('metatrans/metatrans2_cov_length2.csv','w')

lines = f1.readlines()
for line in lines:
	line = line.strip()
	gene = line.split(',')[0]
	rpkm = line.split(',')[3]
	if "Bin01.2" in gene:
		rpkm_g = float(rpkm)/321.38
		f3.write(line+str(321.38)+','+str(rpkm_g)+'\n')
	if "Bin02.1" in gene:
		rpkm_g = float(rpkm)/751.69
		f3.write(line+str(751.69)+','+str(rpkm_g)+'\n')
	if "Bin03.6" in gene:
		rpkm_g = float(rpkm)/60.56
		f3.write(line+str(60.56)+','+str(rpkm_g)+'\n')
	if "Bin26.3" in gene:
		rpkm_g = float(rpkm)/104.55
		f3.write(line+str(104.55)+','+str(rpkm_g)+'\n')
	if "Bin31.4" in gene:
		rpkm_g = float(rpkm)/31.70
		f3.write(line+str(31.70)+','+str(rpkm_g)+'\n')
	if "Bin32.1" in gene:
		rpkm_g = float(rpkm)/20.91
		f3.write(line+str(20.91)+','+str(rpkm_g)+'\n')

lines = f2.readlines()
for line in lines:
	line = line.strip()
	gene = line.split(',')[0]
	rpkm = line.split(',')[3]
	if "Bin01.2" in gene:
		rpkm_g = float(rpkm)/321.38
		f4.write(line+str(321.38)+','+str(rpkm_g)+'\n')
	if "Bin02.1" in gene:
		rpkm_g = float(rpkm)/751.69
		f4.write(line+str(751.69)+','+str(rpkm_g)+'\n')
	if "Bin03.6" in gene:
		rpkm_g = float(rpkm)/60.56
		f4.write(line+str(60.56)+','+str(rpkm_g)+'\n')
	if "Bin26.3" in gene:
		rpkm_g = float(rpkm)/104.55
		f4.write(line+str(104.55)+','+str(rpkm_g)+'\n')
	if "Bin31.4" in gene:
		rpkm_g = float(rpkm)/31.70
		f4.write(line+str(31.70)+','+str(rpkm_g)+'\n')
	if "Bin32.1" in gene:
		rpkm_g = float(rpkm)/20.91
		f4.write(line+str(20.91)+','+str(rpkm_g)+'\n')

f1.close()
f2.close()
f3.close()
f4.close()
