#-----------------------------------------------------------------------------------
#22. カテゴリ名の抽出
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import nlp20
import re

lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

for line in lines:
    if "Category" in line:#取得結果からCategoryのみ抽出して出力
        #[[Category:イギリス|*]] を正規表現で イギリス のみ取り出し
        # :と|と]で挟まれているので、それを抜出
        m = re.split(r'[:|\]]', line) # ] の前にバックスラッシュ
        if m:
        	print(m[1]) 
        else:
            print("none!") 

