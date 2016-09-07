
#-----------------------------------------------------------------------------------
#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．

import nlp20
import re

lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

for line in lines:
    if "ファイル:" in line:#取得結果から「ファイル:」で抽出
        m = re.split(r'[|]', line)
        if m:
            print(m[0]) 
        else:
            print("none!") 

