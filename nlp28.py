#-----------------------------------------------------------------------------------
#28. MediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import nlp20
import re

#参考：http://qiita.com/gamma1129/items/68e955853e265cb12ebe
def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str) # ' を除去
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str) # [ ] で囲まれた箇所を除去
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str) #★ { } 
    str = re.sub(r"<.*?>", r"", str) #★タグ
    str = re.sub(r"\[.*?\]", r"", str)#★ [ ]の残り
    return str

lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

dic = {} #辞書

for line in lines:
    if " = " in line:#取得結果から「 = 」で抽出
        m = re.split(r' = ', line)
        if m:
            dic[m[0].replace("\a", "")] = remove_markup(m[1]) #置換して格納
        else:
            print("none!") 
            
print(dic)

