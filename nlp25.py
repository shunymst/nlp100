#-----------------------------------------------------------------------------------
#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import nlp20
import re


lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

#辞書
dic = {}

for line in lines:
    if " = " in line:#取得結果から「 = 」で抽出
        m = re.split(r' = ', line)
        if m:
            dic[m[0]] = m[1] #追加
        else:
            print("none!") 
            
print(dic)
    
