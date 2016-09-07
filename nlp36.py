
#-----------------------------------------------------------------------------------
#36. 単語の出現頻度
#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
import MeCab
import ngram
import numpy as np
import nlp30
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties

def get_frequency(words: list) -> dict:
    """
    単語のリストを受け取って、単語をキーとして、頻度をバリューとする辞書を返す.
    :param words 単語のリスト
    :return dict 単語をキーとして、頻度をバリューとする辞書
    """
    frequency = {}
    for word in words:
        if frequency.get(word):
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [nlp30.tabbed_str_to_dict(line) for line in file_wrapper]

frequency = get_frequency([morpheme['surface'] for morpheme in morphemes])

# ソート
frequency = [(k, v) for k, v in sorted(frequency.items(), key=lambda x: x[1], reverse=True)]

# 結果の確認
print(frequency[0:20])
