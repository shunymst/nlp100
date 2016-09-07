


#-----------------------------------------------------------------------------------
#35. 名詞の連接
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
import MeCab
import ngram
import numpy as np
import nlp30
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties

def morphemes_to_noun_array(morphemes: list) -> list:
    """
    辞書型で表された形態素のリストを句点もしくは名詞以外の形態素で区切ってグルーピングし、リスト化する.
    :param morphemes 辞書型で表された形態素のリスト
    :return 名詞の連接のリスト
    """
    nouns_list = []
    nouns = []

    for morpheme in morphemes:
        if morpheme['pos1'].find('名詞') >= 0:
            nouns.append(morpheme)
        elif (morpheme['pos1'] == '記号-句点') | (morpheme['pos1'].find('名詞') < 0):
            nouns_list.append(nouns)
            nouns = []

    return [nouns for nouns in nouns_list if len(nouns) > 1]

with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [nlp30.tabbed_str_to_dict(line) for line in file_wrapper]


noun_array = [''.join([noun['surface'] for noun in nouns]) for nouns in morphemes_to_noun_array(morphemes)]

# 結果の確認
print(noun_array[::100])

