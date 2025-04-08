import sys
import re
# This script extracts genes with TATA boxes from a FASTA file and writes them to a new file.
# It uses regular expressions to find TATA boxes in the gene sequences.
gene_name=[]
gene_seq=[]
input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open('tata_genes.fa','w')
m=-1
# Read the input FASTA file and extract gene names and sequences
# The input file is expected to be in FASTA format with gene names in the header lines
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