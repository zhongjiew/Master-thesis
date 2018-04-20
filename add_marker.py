
for i in range(1, 41):
	f1 = open('bacteria_and_archaea_dir/BA%05d.faa'%i, 'r')
	f2 = open('40add_marker/BA000%s_addmarker.faa'%i, 'w')

	seqlist = f1.readlines()
	for line in seqlist:
		if line.startswith('>'):
			line = line.replace('>', '>marker%s_'%i)

		f2.write(line)

f1.close()
f2.close()
