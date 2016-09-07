#-----------------------------------------------------------------------------------
#23. セクション構造
#記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import nlp20
import re

lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

for line in lines:
    if "==" in line:#取得結果から「=」で抽出
        lv = len(re.findall(r'[=]', line)) / 2 #LVの取得
        print(line + " LV=" + str(lv)) 
