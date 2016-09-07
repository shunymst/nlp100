#-----------------------------------------------------------------------------------
#27. 内部リンクの除去
#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import nlp20
import re

def remove_markup(str):#参考：http://qiita.com/gamma1129/items/68e955853e265cb12ebe
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    return str

lines = nlp20.getUK().split("\n")#importしてモジュール呼び出し

dic = {} #辞書

for line in lines:
    if " = " in line:#取得結果から「 = 」で抽出
        m = re.split(r' = ', line)
        if m:
            dic[m[0].replace("\a", "")] = remove_markup(m[1]) #★置換して格納
        else:
            print("none!") 
            
print(dic)
