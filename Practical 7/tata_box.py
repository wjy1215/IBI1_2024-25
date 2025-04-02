import sys
import re
gene_name=[]
gene_seq=[]
input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open('tata_genes.fa','w')
m=-1
for line in input:
    if  re.search(r'gene:',line):
        name=re.findall(r'gene:([^:\s]+)',line)
        n=''.join(map(str, name))
        gene_name.append(n)
        gene_seq.append('')
        m+=1
    else:
        gene_seq[m]+=line.strip()
        #if e.search(r'TATA[TA]A[Tnot rA]',seq):
for i in range (m):
    if re.search(r'TATA[TA]A[TA]',gene_seq[i]):
        output.write('>'+gene_name[i]+'\n')
        output.write(gene_seq[i]+'\n')
input.close()
output.close()