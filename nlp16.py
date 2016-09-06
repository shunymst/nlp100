#================================================================================
#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys
import subprocess

param = sys.argv
filename = param[1]
devidecnt = param[2]

#python nlp16.py hightemp.txt 3
f = open(filename, 'r')
line = f.readline()

lines = f.readlines()
linerow = len(lines)#行数取得

for i in range(int(devidecnt)):#分割指定数分ループ
     print("devide!")
     print(lines[i], end="")      
f.close()

#split -l 5 hightemp.txt
print("コマンドで確認")
subprocess.call( ["split", "-l", devidecnt, filename] )

