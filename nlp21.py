#-----------------------------------------------------------------------------------
#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．

import nlp20

lines = nlp20.getUK().split("\n")

for line in lines:
    if "Category" in line:
        print(line)

