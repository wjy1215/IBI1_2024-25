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
seq_human = read_fasta("Human.fasta")
seq_mouse= read_fasta("Mouse.fasta")
seq_random = read_fasta("random.fasta")
# human and mouse
blosum_score1, identical1 = blosum_score(seq_human, seq_mouse)
pre_identity1 = identical1 / len(seq_human) * 100
# human and random
blosum_score2, identical2 = blosum_score(seq_human, seq_random)
pre_identity2 = identical2 / len(seq_human) * 100
# mouse and random
blosum_score3, identical3 = blosum_score(seq_mouse, seq_random)
pre_identity3 = identical3 / len(seq_mouse) * 100
# Print the results
print("The blosum score betweenseq_human and seq_mouse is:", blosum_score1)  #  score:human and mouse 
print("The pre_identity betweenseq_human and seq_mouse is:", pre_identity1)  #  pre_identity:human and mouse
print("The blosum score betweenseq_human and seq_random is:", blosum_score2)  #  score:human and random
print("The pre_identity betweenseq_human and seq_random is:", pre_identity2)  #  pre_identity:human and random
print("The blosum score between seq_mouse and seq_random is:", blosum_score3)  #  score:mouse and random
print("The pre_identity between seq_mouse and seq_random is:", pre_identity3)  #  pre_identity:mouse and random
