#================================================================================
#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
txt = "hightemp.txt"
import subprocess
import sys

list = []

r = open(txt).readlines()

for l in r:
	s = l.split('\t')
	#c1.write(s[0]+'\n')
	list.append(s[2])
		
print(sorted(list, reverse=True))




print("コマンドで確認")
cmd = "cut -f3 hightemp.txt | sort -r -n"
subprocess.call( cmd.strip().split(" ")  ) 

