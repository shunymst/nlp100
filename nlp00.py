#00. 文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

tgt = "stressed"

#a[n]          # 文字列 a の中の n 番目の文字を取り出します
#print(tgt[8]) IndexError: string index out of range
print("★古典的、固定的なやりかた")
print(tgt[7]+tgt[6]+tgt[5]+tgt[4]+tgt[3]+tgt[2]+tgt[1]+tgt[0])

 
print("★文字列長取得してfor文で")
len = len(tgt) 
answer = ""
for num in range(len-1, -1, -1): #http://d.hatena.ne.jp/emergent/20101031/1288532125
  answer = answer + tgt[num]
print(answer)

# 文字列インデックス[開始インデックス:終了インデックス:ステップ数]
print("★スライスで")
print(tgt[::-1])
