#================================================================================
#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys
import subprocess

param = sys.argv
filename = param[1]

#python nlp15.py hightemp.txt
f = open(filename, 'r')
line = f.readline()

lines = f.readlines()
linerow = len(lines)

for i in range(linerow-5, linerow):
     print(lines[i], end="")
f.close()

print("コマンドで確認")
subprocess.call( ["tail", "-5", filename] ) 

