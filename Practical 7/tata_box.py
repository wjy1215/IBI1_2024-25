import sys
import re
import os
os.chdir('practical 7')
# This script extracts genes with TATA boxes from a FASTA file and writes them to a new file.
# It uses regular expressions to find TATA boxes in the gene sequences.
intput_file_path = r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file_path = r'tata_genes.fa'
gene_seq=[]
gene_name=[]
input=open(r"C:\cygwin64\home\wjyibi\IBI1_2024-25\Practical 7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
output=open(r'C:\cygwin64\home\wjyibi\IBI1_2024-25\Practical 7\tata_genes.fa','w')
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