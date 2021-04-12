import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from Bio import SeqIO

window = 1000
step = 300

fasta_in = sys.argv[1]

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

num = len(seq)  #与えられたDNA配列の文字数
list_x = []
list_y = []

for i in range(0,num,step):
    num_gc = 0
    if i+window > num:  #一番最後の処理
        for char in seq[i:num]:
            if char == 'G' or char == 'C':
                num_gc += 1
        list_x.append(i)
        list_y.append(num_gc/(num-i))
        break
    for char in seq[i:(i+window)]:
        if char == 'G' or char == 'C':
            num_gc += 1
    list_x.append(i)
    list_y.append(num_gc/1000)

fig = plt.figure(figsize=(6.4,4.8),dpi=100,facecolor='w')
ax = fig.add_subplot(111,title='W:'+str(window)+' S:'+str(step),fc='w',ylabel='percentage of GC')
ax.plot(list_x,list_y)

fig.savefig('percentage_of_GC.png')
