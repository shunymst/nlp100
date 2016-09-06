#================================================================================
#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
txt = "hightemp.txt"
import subprocess
import sys

list = []

r = open(txt).readlines()

for l in r:
	s = l.split('\t')
	#c1.write(s[0]+'\n')
	list.append(s[0])
		
list.sort()
print(list)

print("模範解答")#http://qiita.com/Ria0130/items/7573302aa48edfe94c36
r = open(txt).readlines()
print('\n'.join(set((x.split('\t')[0] for x in r))))

print("コマンドで確認")
cmd = "cut -f1 hightemp.txt | sort | uniq -c"
subprocess.call( cmd.strip().split(" ")  ) 
#subprocess.call( ["cut", "-f1", txt, "|", "sort", "|", "uniq", "-c"] )



