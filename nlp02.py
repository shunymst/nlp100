#-----------------------------------------------------------------------------------
#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

tgt1 = "パトカー"
tgt2 = "タクシー"

print("★古典的、固定的なやりかた")
print(tgt1[0]+tgt2[0]+tgt1[1]+tgt2[1]+tgt1[2]+tgt2[2]+tgt1[3]+tgt2[3])

print("★zip関数で複数の引数を同時にループで回す")
answer = ""
for char1, char2 in zip(tgt1, tgt2):
    answer = answer + char1 + char2
print(answer)

print("★にjoinでがっちゃんこで省メモリ…だそうな")
print(''.join([char1 + char2 for char1, char2 in zip(tgt1, tgt2)]))

