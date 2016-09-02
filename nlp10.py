#================================================================================
#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．
txt = "hightemp.txt"

#print(num_lines = sum(1 for line in open('hightemp.txt')))
print(len(open(txt).readlines()))

import subprocess
subprocess.call( ["wc", "-l", txt] ) 
