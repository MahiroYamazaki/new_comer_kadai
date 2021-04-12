import sys
from Bio import SeqIO

fasta_in = sys.argv[1]
num_a = 0
num_t = 0
num_g = 0
num_c = 0

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

for char in seq:
    if char == 'A':
        num_a += 1
    elif char == 'T':
        num_t += 1
    elif char == 'G':
        num_g += 1
    elif char == 'C':
        num_c += 1

print('A:' + str(num_a) + ' T:' + str(num_t) + ' G:' + str(num_g) + ' C:' + str(num_c))
