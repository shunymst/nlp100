

#-----------------------------------------------------------------------------------
#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

#http://www.shuiren.org/chuden/teach/n-gram/index-j.html
#N-gramモデルとは、「ある文字列の中で、N個の文字列または単語の組み合わせが、どの程度出現するか」を調査する言語モデルを意味します。
#任意のn文字の連続は、n-gramと呼ばれる

#http://www.sophia-it.com/content/bigram
#bigram バイグラム…任意の文字列が2文字だけ続いた文字列のことである。
#['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er'] 文字で2つずつ
#['I-am', 'am-an', 'an-NLPer'] 単語で2つずつ

sentence="I am an NLPer"

#文字bi-gram
charGram=[sentence[i:i+2] for i in range(len(sentence)-1)] #1つずつずれて2文字ずつ取得しているだけ

#単語bi-gram
words=[word.strip(".,") for word in sentence.split()] 
wordGram=["-".join(words[i:i+2]) for i in range(len(words)-1)] #こっちも同じ

print(charGram)
print(wordGram)

