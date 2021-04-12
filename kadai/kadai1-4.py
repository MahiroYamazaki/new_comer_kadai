import sys
from Bio import SeqIO

fasta_in = sys.argv[1]
part = sys.argv[2]

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

list = []
list_rev = []

for i in range(len(seq)-len(part)+1):
    for j in range(len(part)):
        if seq[i+j] != part[j]:
            break
        if j == (len(part)-1):
            list.append(i+1)

for i in range(len(seq)-len(part)+1):
    for j in range(len(part)):
        if rev[i+j] != part[j]:
            break
        if j == (len(part)-1):
            list_rev.append(i+1)

print('')
print('部分配列が与えられた配列と一致する先頭の位置')
print(list)
print('')
print('部分配列が逆相補鎖と一致する先頭の位置')
print(list_rev)
print('')
