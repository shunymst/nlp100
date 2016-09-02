


#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
#XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


sentence1="paraparaparadise"
sentence2="paragraph"

#文字bi-gramは文字で2つずつ
charGramX=[sentence1[i:i+2] for i in range(len(sentence1)-1)] 
charGramY=[sentence2[i:i+2] for i in range(len(sentence2)-1)] 


#XとYの
#和集合 要素全体の集合
#積集合 共通部分の集合
#差集合 他の集合を除いた要素の集合
sX = set(charGramX)
sY = set(charGramY)

print("★和集合")
print(sX.union(sY))

print("★差集合")
print(sX.difference(sY))

print("★積集合")
print(sX.intersection(sY))


#さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ
tgt = set(["se"])

#TypeError: Can't convert 'bool' object to str implicitly
#print("★'se'がXおよびYに含まれるか [" + tgt.issubset(sX) + "] [" + tgt.issubset(sY) + "]" )

print("★'se'がXおよびYに含まれるか [" + str(tgt.issubset(sX)) + "] [" + str(tgt.issubset(sY)) + "]" )

