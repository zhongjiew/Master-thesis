### extract orthologous gene cluster into files ###

f1 = open('match_orth_nameI12', 'r')
f2 = open('all42orf.fasta', 'r')
orths = f1.readlines()
fasta = f2.read().split('>')
i = 1

for orthline in orths:
    orthline = orthline.strip().split('\t')
    for orth in orthline:
        for gene in fasta:
            genename = gene.split('\n')
            if orth == genename[0]:
                f3 = open('ortholog%s.fasta' %str(i), 'a+')
                f3.write('>'+'%s\n' %gene)
                f3.close()
    i += 1
f1.close()
f2.close()

