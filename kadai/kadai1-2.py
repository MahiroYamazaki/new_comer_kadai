import sys
from Bio import SeqIO

fasta_in = sys.argv[1]

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

rev = ''

for char in seq:
    if char == 'A':
        rev = 'T' + rev
    elif char == 'T':
        rev = 'A' + rev
    elif char == 'G':
        rev = 'C' + rev
    elif char == 'C':
        rev = 'G' + rev

print(rev)
