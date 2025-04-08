def find_restriction_sites(dna_sequence, recognition_sequence):
    sites = []
    pos = dna_sequence.find(recognition_sequence)
    while pos != -1:
        sites.append(pos)
        pos = dna_sequence.find(recognition_sequence, pos + 1)
        return sites
    return 'NOT_FOUND'
seq=input("Enter the DNA sequence: ").upper()
rec_seq=input("Enter the recognition sequence: ").upper()
valid_nucleotides = {'A', 'C', 'G', 'T'}
if not set(seq).issubset(valid_nucleotides):
    raise ValueError("DNA sequence contains non-canonical nucleotides.")
    print("DNA sequence contains non-canonical nucleotides.")
    exit()
if not set(rec_seq).issubset(valid_nucleotides):
    raise ValueError("Recognition sequence contains non-canonical nucleotides.")
    print("Recognition sequence contains non-canonical nucleotides.")
    exit()
find_restriction_sites(seq, rec_seq)
print(f"Restriction sites for {rec_seq} in the DNA sequence are at positions: {find_restriction_sites(seq, rec_seq)}")
# Example usage
dna_sequence = "ACGTACGTGACGTA"
recognition_sequence = "CGT"
restriction_sites = find_restriction_sites(dna_sequence, recognition_sequence)
print(f"EXAMPLE : Restriction sites for {recognition_sequence} in the DNA sequence are at positions: {restriction_sites}")


