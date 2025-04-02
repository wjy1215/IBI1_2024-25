import re
splice_combination = input("Enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC): ").strip().upper()
valid_combinations = {"GTAG", "GCAG", "ATAC"}
if splice_combination not in valid_combinations:
    print("Invalid combination. Please enter one of GTAG, GCAG, or ATAC.")
    exit(1)
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = f'{splice_combination}_spliced_genes.fa'
gene_name = []
gene_seq = []
current_name = None
current_sequence = ''
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
if current_name is not None:
    gene_name.append(current_name)
    gene_seq.append(current_sequence)
tata_pattern = re.compile(r'TATA[AT][AT]')
with open(output_file, 'w') as fasta_out:
    for name, seq in zip(gene_name, gene_seq):
        if tata_pattern.search(seq) and splice_combination in seq:
            tata_count = len(tata_pattern.findall(seq))
            fasta_out.write(f'>{name}_TATA_count:{tata_count}\n{seq}\n')
print(f"Output written to {output_file}")
