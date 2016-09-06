

#================================================================================
#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
txt = "hightemp.txt"
import subprocess

#f = open(txt)
#lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
#f.close()
#print (str(lines2).replace('\t', ' '))
#上記だとこのようにになってしまう　改行文字もそのまま読まれてしまうから→['高知県\t江川崎\t41\t2013-08-12\n', 略, '愛知県\t名古屋\t39.9\t1942-08-02\n', '\n']

print(open(txt).read().replace('\t', ' '))

print("コマンドで確認")
#sed 's/\t/ /g' hightemp.txt
import subprocess
subprocess.call( ["sed", "s/\t/ /g", txt] ) 

