file_name1=raw_input("Enter the full name of the txt file that contains ID: ")
file_name2=raw_input("Enter the full name of the fasta file: ") 
file_name3=raw_input("Enter the name of output file(.fasta): ")
from Bio import SeqIO 
fileinput =open(file_name1,'r')
fileoutput=open(file_name3,'w')

print 'The Python script is running... Pls wait!'

a=[]
for line in open(file_name1,'r'):
    a.append(str(line).strip())


Num=0
for record in SeqIO.parse(file_name2,'fasta'):
    Num+=1    
    if str(record.id).strip() in a:
        fileoutput.write('>'+str(record.id).strip()+'\n')
        fileoutput.write(str(record.seq).strip()+'\n')
    if Num%100000==0:
        print Num, 'records have been processed!'

print 'OK, Finished!'
