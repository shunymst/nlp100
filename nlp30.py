#-----------------------------------------------------------------------------------
#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
#ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
#1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
[
	{'base': 'イチ'
	'pos': '一'
	'surface': '一'
	'pos1': '名詞-数'}
	{'base': ''
	'pos': ''
	'surface': '記号-空白'
	'pos1': ''}
	{'base': 'ワガハイ'
	'pos': '吾輩'
	'surface': '吾輩'
	'pos1': '名詞-代名詞-一般'}
	{'base': 'ハ'
	'pos': 'は'
	'surface': 'は'
	'pos1': '助詞-係助詞'}
	{'base': 'ネコ'
	'pos': '猫'
	'surface': '猫'
	'pos1': '名詞-一般'}
	{'base': 'デ'
	'pos': 'だ'
	'surface': 'で'
	'pos1': '助動詞'}
	{'base': 'アル'
	'pos': 'ある'
	'surface': 'ある'
	'pos1': '助動詞'}
	{'base': '。'
	'pos': '。'
	'surface': '。'
	'pos1': '記号-句点'}★区切り
]
"""
import MeCab
import ngram
import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties

#吾輩    ワガハイ        吾輩    名詞-代名詞-一般
#は      ハ      は      助詞-係助詞
#猫      ネコ    猫      名詞-一般

def tabbed_str_to_dict(tabbed_str: str) -> dict:
    """
    例えば「次第に   シダイニ    次第に   副詞-一般   」のようなタブ区切りで形態素を表す文字列をDict型に変換する.
    :param tabbed_str タブ区切りで形態素を表す文字列
    :return Dict型で表された形態素
    """
    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def morphemes_to_sentence(morphemes: list) -> list:
    """
    Dict型で表された形態素のリストを句点毎にグルーピングし、リスト化する.
    :param morphemes Dict型で表された形態素のリスト
    :return 文章のリスト
    """
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences


with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]

sentences = morphemes_to_sentence(morphemes)

# 結果の確認
print(morphemes[::20])
print(sentences[::20])
