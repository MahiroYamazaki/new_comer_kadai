import sys
from Bio import SeqIO

fasta_in = sys.argv[1]
part = sys.argv[2]

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

def reverse(text):
    ans = ''
    for char in text:
        if char == 'A':
            ans = 'T' + ans
        elif char == 'T':
            ans = 'A' + ans
        elif char == 'G':
            ans = 'C' + ans
        elif char == 'C':
            ans = 'G' + ans
    return ans

rev = reverse(seq)

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
