#================================================================================
#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
txt = "hightemp.txt"
import subprocess

f = open(txt)
lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()

print (str(lines2).replace("\t", " "))



print("コマンドで確認")
#import subprocess
#subprocess.call( ["wc", "-l", txt] ) 



