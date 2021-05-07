import sys
import math
import pymol

#条件を設定
f_name = '1buw.pdb'  #ファイル名
chain_name = 'A'  #鎖名
g_x = 47.04  #重心の座標
g_y = 33.34
g_z = 35.57
r_r = 14.59  #回転半径(rotation radius)
#ここまで

id = f_name[0:4]  #id
fp = open(f_name)
pdb = fp.read()  #pdb
fp.close()

pdb = pdb.split("\n")  #行ごとに分割

atom_list = []  #鎖の原子リスト

for l in pdb:
    if (l[0:4] == 'ATOM' or l[0:6] == 'HETATM') and l[21] == chain_name:
        x = l[30:38].replace(' ','')
        y = l[38:46].replace(' ','')
        z = l[46:54].replace(' ','')
        r = math.sqrt((float(x) - g_x)**2 + (float(z) - g_z)**2 + (float(z) - g_z)**2)
        if r < r_r:
            atom_list.append(l)

# pymol.cmd.select('atoms','id 9999')

for l in atom_list:
    id = 'id ' + str(l[7:11].replace(' ',''))
    pymol.cmd.select('atoms',id)
    pymol.cmd.color('red','atoms')
