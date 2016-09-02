#-----------------------------------------------------------------------------------
#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．
#適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
#を与え，その実行結果を確認せよ．
from random import shuffle
import random

def shuffle(word):

	#TypeError: 'list' object is not callable ★未成功　listがlistコマンドとして認識されない
	#word_list = list(word)
	word_list = list(str(word))
	middle = word_list[1:-1]
	random.shuffle(middle)#シャッフル
	print(middle)	
	
	return word[0]+''.join(middle)+word[-1]
    
def convert(x):
    #return ''.join("★"+c if len(c)>=4 else c for c in x) #長さ4以上の場合は★つける　とりあえず
    #return ''.join(shuffle(c) if len(c)>=4 else c for c in x) #並び替える NG→stringをシャッフルできない
    return ' '.join(shuffle(c) if len(c)>=4 else c for c in x)#ので、長さ4以上の場合のシャッフルを別関数に！
    
if __name__=="__main__":
	tgt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

	#単語で分ける
	print("★, .を除去、スペースで区切る　まで")
	tgt2 = tgt.translate(str.maketrans('', '', ',.'))
	list = tgt2.split()
	
	#関数実行
	result = convert(list)
	print(result)



