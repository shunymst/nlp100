
#================================================================================
#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
txt = "hightemp.txt"
import subprocess
import sys

print("模範解答")#http://qiita.com/Ria0130/items/7573302aa48edfe94c36
r = [s.split('\t')[0] for s in open(txt)] #1要素目を取得
c = {k:r.count(k) for k in r} #sortかける
s = sorted(c, key=lambda k:c[k], reverse=True)
print('\n'.join(str(c[k])+' '+k for k in s))


print("コマンドで確認")
cmd = "cut -f 1 hightemp.txt | sort | uniq -c | sort -r"
subprocess.call( cmd.strip().split(" ")  ) 
#cut: invalid option -- 'r' 怒られる | が原因？？

