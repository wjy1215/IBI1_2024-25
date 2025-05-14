import re
import os
os.chdir('practical 7')
splice_combination = input("Enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC): ").strip().upper()
valid_combinations = {"GTAG", "GCAG", "ATAC"}
doner=splice_combination[:2]
acceptor=splice_combination[2:]
# Define the regular expression pattern for the splice donor and acceptor sites
# Check if the input is valid
if splice_combination not in valid_combinations:
    print("Invalid combination. Please enter one of GTAG, GCAG, or ATAC.")
    exit(1)
input_file=r"C:\cygwin64\home\wjyibi\IBI1_2024-25\Practical 7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file=rf'C:\cygwin64\home\wjyibi\IBI1_2024-25\Practical 7\{splice_combination}_spliced_genes.fa'
gene_name = []
gene_seq = []
current_name = None
current_sequence = ''
# Read the input FASTA file and extract gene names and the sequences
# The input file is expected to be in FASTA format with gene names in the header lines
with open(input_file, 'r') as fasta_in:
    for line in fasta_in:
        line = line.strip()
        if line.startswith('>'):
            if current_name is not None:
                gene_name.append(current_name)
                gene_seq.append(current_sequence)
            current_name = re.findall(r'gene:([^:\s]+)', line)
            if current_name:
                current_name = current_name[0]
            current_sequence = ''
        else:
            current_sequence += line.strip()
    # Append the last gene sequence if it exists
if current_name is not None:
    gene_name.append(current_name)
    gene_seq.append(current_sequence)
tata_pattern = re.compile(r'TATA[AT]A[AT]')
# Write the output to a new FASTA file with TATA box count in the header
# The output file will contain only the genes that have TATA boxes and the specified splice combination
with open(output_file, 'w') as fasta_out:
    for name, seq in zip(gene_name, gene_seq):
        if tata_pattern.search(seq) and re.search(rf'{doner}[ATCG]+{acceptor}', seq):
            tata_count = len(tata_pattern.findall(seq))
            fasta_out.write(f'>{name}_TATA_count:{tata_count}\n{seq}\n')
print(f"Output written to {output_file}")
