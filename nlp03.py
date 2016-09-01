#-----------------------------------------------------------------------------------
#03. 円周率
# I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

print("★, .を除去")
tgt = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tgt2 = tgt.translate(str.maketrans('', '', ',.')) #http://orangain.hatenablog.com/entry/20100503/1272900555
print(tgt2)

print("★スペースで区切る")
print(tgt2.split())

print("★単語数")
print(len(tgt2.split()))

print("★文字数")
for char in tgt2.split():
    print(len(char))

