#================================================================================
#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

#txt = "hightemp.txt"
import subprocess

c1 = open('col1.txt').readlines()
c2 = open('col2.txt').readlines()

with open('colmerge.txt', 'w') as cm:
	for s1, s2 in zip(c1, c2):
    	#print(s1.rstrip() + '\t' + s2.rstrip())
		cm.write(s1.rstrip() + '\t' + s2.rstrip()+'\n')

print("コマンドで確認 colmerge.txt")
subprocess.call( ["cat", "colmerge.txt", ] ) 
print("コマンドで確認 paste")
subprocess.call( ["paste", "col1.txt", "col2.txt"] ) 


