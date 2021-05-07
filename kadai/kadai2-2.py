import sys
import math

id = sys.argv[1][0:4]  #id
fp = open(sys.argv[1])  #ファイル名
chain_name = sys.argv[2]  #鎖名
pdb = fp.read()  #pdb
fp.close()

pdb = pdb.split("\n")

weight = {  #対応する原子量
    'C':'12' , 'N':'14', 'O':'16', 'S':'32', 'FE':'56'
}

atom_list = []  #鎖の原子リスト

cnt_x = 0  #重心(center)
cnt_y = 0
cnt_z = 0

total_weight = 0  #合計の重さ

for l in pdb:
    if (l[0:4] == 'ATOM' or l[0:6] == 'HETATM') and l[21] == chain_name:
        atom_list.append(l)
        w = int(weight[l[76:78].replace(' ','')])
        x = l[30:38].replace(' ','')
        y = l[38:46].replace(' ','')
        z = l[46:54].replace(' ','')
        cnt_x = w * float(x) + cnt_x
        cnt_y = w * float(y) + cnt_y
        cnt_z = w * float(z) + cnt_z
        total_weight = total_weight + w

cnt_x = cnt_x / total_weight  #ここで重心が求まる
cnt_y = cnt_y / total_weight
cnt_z = cnt_z / total_weight

r = 0  #回転半径

for l in atom_list:
    w = int(weight[l[76:78].replace(' ','')])
    x = l[30:38].replace(' ','')
    y = l[38:46].replace(' ','')
    z = l[46:54].replace(' ','')
    r = w * ((float(x) - cnt_x)**2 + (float(y) - cnt_y)**2 + (float(z) - cnt_z)**2) + r

r = math.sqrt(r / total_weight)  #ここで回転半径が求まる

print('x:' + str('{:.2f}'.format(cnt_x)) + ' y:' + str('{:.2f}'.format(cnt_y)) + ' z:' + str('{:.2f}'.format(cnt_z)))
print('{:.2f}'.format(r))  #出力
