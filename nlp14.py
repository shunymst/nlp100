#================================================================================
#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
import sys
import subprocess

param = sys.argv
filename = param[1]

#python nlp14.py hightemp.txt
f = open(filename, 'r')
line = f.readline()
for i in range(0, 4):
    print(line, end="")  #,で改行の重複を防ぐ
    line = f.readline()
f.close()

print("コマンドで確認")
subprocess.call( ["head", "-5", filename] ) 

