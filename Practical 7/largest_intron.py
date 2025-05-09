import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' # DNA sequence
intron=re.findall(r'GT[ATCG]*AG', seq)
print(intron)
print('The largest intron is:', max(intron, key=len))
print('The length of the largest intron is:', len(max(intron, key=len)))    


