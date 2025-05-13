import blosum as bl
import os
os.chdir('practical 13')
matrix = bl.BLOSUM(62) # BLOSUM62 matrix
# this function reads a fasta file and returns the sequence
def read_fasta(filename):
    with open(filename) as f:
        sequence = ''
        for line in f:
            if not line.startswith('>'):
                sequence += line.strip()
        return sequence
# this function calculates the blosum score and the percentage of identical residues
def blosum_score(s1, s2):
    score = 0
    identical = 0
    for a, b in zip(s1, s2):
        if a == b:
            score += matrix[a][b]
            identical +=1
        else:
            score += matrix[a][b]
    return score,identical

seq1 = read_fasta("Human.fasta")
seq2= read_fasta("Mouse.fasta")
seq3 = read_fasta("randam.fasta")
# human and mouse
blosum_score1, identical1 = blosum_score(seq1, seq2)
pre_identity1 = identical1 / len(seq1) * 100
# human and random
blosum_score2, identical2 = blosum_score(seq1, seq3)
pre_identity2 = identical2 / len(seq1) * 100
# mouse and random
blosum_score3, identical3 = blosum_score(seq2, seq3)
pre_identity3 = identical3 / len(seq2) * 100
# Print the results
print("The blosum score between seq1 and seq2 is:", blosum_score1)  #  score:human and mouse 
print("The pre_identity between seq1 and seq2 is:", pre_identity1)  #  pre_identity:human and mouse
print("The blosum score between seq1 and seq3 is:", blosum_score2)  #  score:human and random
print("The pre_identity between seq1 and seq3 is:", pre_identity2)  #  pre_identity:human and random
print("The blosum score between seq2 and seq3 is:", blosum_score3)  #  score:mouse and random
print("The pre_identity between seq2 and seq3 is:", pre_identity3)  #  pre_identity:mouse and random
