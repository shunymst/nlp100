#-----------------------------------------------------------------------------------
#31. 動詞
#動詞の表層形をすべて抽出せよ．
#-----------------------------------------------------------------------------------
#32. 動詞の原形
#動詞の原形をすべて抽出せよ．
#-----------------------------------------------------------------------------------
#33. サ変名詞
#サ変接続の名詞をすべて抽出せよ．

import MeCab
import ngram
import numpy as np
import nlp30
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties

with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [nlp30.tabbed_str_to_dict(line) for line in file_wrapper]
    
verbs_surface = [morpheme['surface'] for morpheme in morphemes if morpheme['pos1'].find('動詞') == 0]
verbs_base = [morpheme['base'] for morpheme in morphemes if morpheme['pos1'].find('動詞') == 0]
nouns_suru = [morpheme['surface'] for morpheme in morphemes if morpheme['pos1'] == '名詞-サ変接続']

# 結果の確認
print(verbs_surface[::20])
print("===========================================")
print(verbs_base[::20])
print("===========================================")
print(nouns_suru[::20])
