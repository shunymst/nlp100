#-----------------------------------------------------------------------------------
#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

#-----------------------------------------------------------------------------------
#38. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

#-----------------------------------------------------------------------------------
#39. Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
import MeCab
import ngram
import numpy as np
import nlp30
import nlp36
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
    morphemes = [nlp30.tabbed_str_to_dict(line) for line in file_wrapper]

frequency = nlp36.get_frequency([morpheme['surface'] for morpheme in morphemes])


fig = plt.figure(figsize=(20, 6))

# 37. 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
words = [f[0] for f in frequency[0:10]]
x_pos = np.arange(len(words))
fp = FontProperties(fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14)

ax1 = fig.add_subplot(131)
ax1.bar(x_pos, [f[1] for f in frequency[0:10]], align='center', alpha=0.4)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(words, fontproperties=fp)
ax1.set_ylabel('Frequency')
ax1.set_title('Top 10 frequent words')

# 38. 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
freq = list(dict(frequency).values())
freq.sort(reverse=True)

ax2 = fig.add_subplot(132)
ax2.hist(freq, bins=50, range=(0, 50))
ax2.set_title('Histogram of word count')
ax2.set_xlabel('Word count')
ax2.set_ylabel('Frequency')

# 39. 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
rank = list(range(1, len(freq) + 1))

ax3 = fig.add_subplot(133)
ax3.plot(freq, rank)
ax3.set_xlabel('Rank')
ax3.set_ylabel('Frequency')
ax3.set_title('Zipf low')
ax3.set_xscale('log')
ax3.set_yscale('log')

fig.savefig('morphological_analysis.png')
