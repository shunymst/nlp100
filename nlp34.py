#-----------------------------------------------------------------------------------
#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．

import MeCab
import ngram
import numpy as np
import nlp30
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties


def ngramed_list(lst: list, n: int = 3) -> list:
    """
    listをNグラム化する.
    :param lst Nグラム化対象のリスト
    :param n N (デフォルトは N = 3)
    :return Nグラム化済みのリスト
    """
    index = ngram.NGram(N=n)
    return [term for term in index.ngrams(lst)]


def is_noun_no_noun(words: list) -> bool:
    """
    3つの単語から成るリストが「名詞-の-名詞」という構成になっているかを判定する.
    :param words 3つの単語から成るリスト
    :return bool (True:「名詞-の-名詞」という構成になっている / False:「名詞-の-名詞」という構成になっていない)
    """
    return (type(words) == list) and (len(words) == 3) and \
           (words[0]['pos1'].find('名詞') == 0) and \
           (words[1]['surface'] == 'の') and \
           (words[2]['pos1'].find('名詞') == 0)


with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [nlp30.tabbed_str_to_dict(line) for line in file_wrapper]


# 「名詞-の-名詞」を含むNグラムのみを抽出
noun_no_noun = [ngrams for ngrams in ngramed_list(morphemes) if is_noun_no_noun(ngrams)]# Nグラム化して順にis_noun_no_nounか判定
   
print(noun_no_noun[::20])
print("--------------------------")


# 表層を取り出して結合する
noun_no_noun = [''.join([word['surface'] for word in ngram]) for ngram in noun_no_noun]#

# 結果の確認
print(noun_no_noun[::20])



