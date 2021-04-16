import sys
from Bio import SeqIO

fasta_in = sys.argv[1]

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

def reverse(text):
    ans = ' '
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

def conversion(text,mod,check):
    if check == 0:
        if mod == 0:
            f_name = "3n"
            mod = 2
        else:
            f_name = "3n+" + str(mod)
            mod = mod - 1
    elif check == 1:
        text = reverse(text)
        if mod == 0:
            f_name = "3n_rev"
            mod = 2
        else:
            f_name = "3n+" + str(mod) + "_rev"
            mod = mod - 1
    f = open(f_name,'w')
    f.write("")
    ans = ''
    for i in range(mod,len(text),3):
        if text[i:i+3] == "ATG":
            ans = ans + str(i+1) + " "
            for j in range(i,len(text),3):
                if text[j:j+3] == "TTT" or text[j:j+3] == "TTC":
                    ans = ans + "F"
                elif text[j:j+3] == "TTA" or text[j:j+3] == "TTC" or text[j:j+2] == "CT":
                    ans = ans + "L"
                elif text[j:j+3] == "ATT" or text[j:j+3] == "ATC" or text[j:j+3] == "ATA":
                    ans = ans + "I"
                elif text[j:j+3] == "ATG":
                    ans = ans + "M"
                elif text[j:j+2] == "GT":
                    ans = ans + "V"
                elif text[j:j+3] == "AGT" or text[j:j+3] == "AGC" or text[j:j+2] == "TC":
                    ans = ans + "S"
                elif text[j:j+2] == "CC":
                    ans = ans + "P"
                elif text[j:j+2] == "AC":
                    ans = ans + "T"
                elif text[j:j+2] == "GC":
                    ans = ans + "A"
                elif text[j:j+3] == "TAT" or text[j:j+3] == "TAC":
                    ans = ans + "Y"
                elif text[j:j+3] == "TAA" or text[j:j+3] == "TAG" or (text[j:j+3] == "TGA"):
                    ans = ans + "_"
                    break
                elif text[j:j+3] == "CAT" or text[j:j+3] == "CAC":
                    ans = ans + "H"
                elif text[j:j+3] == "CAA" or text[j:j+3] == "CAG":
                    ans = ans + "Q"
                elif text[j:j+3] == "AAT" or text[j:j+3] == "AAC":
                    ans = ans + "N"
                elif text[j:j+3] == "AAA" or text[j:j+3] == "AAG":
                    ans = ans + "K"
                elif text[j:j+3] == "GAT" or text[j:j+3] == "GAC":
                    ans = ans + "D"
                elif text[j:j+3] == "GAA" or text[j:j+3] == "GAG":
                    ans = ans + "E"
                elif text[j:j+3] == "TGT" or text[j:j+3] == "TGC":
                    ans = ans + "C"
                elif text[j:j+3] == "TGG":
                    ans = ans + "W"
                elif text[j:j+3] == "AGA" or text[j:j+3] == "AGG" or text[j:j+2] == "CG":
                    ans = ans + "R"
                elif text[j:j+2] == "GG":
                    ans = ans + "G"
            ans = ans + "\n"
            f.write(ans)
            ans = ''
            i = i + j
    f.close()

for i in range(0,3):
    for j in range(0,2):
        conversion(seq,i,j)
