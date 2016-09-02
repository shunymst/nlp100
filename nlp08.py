#-----------------------------------------------------------------------------------
#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

#--------------------------------


#219 - 文字コード 　とは？
#chr(219-ord(c) ord: アスキーコードを取得 / chr: アスキーコードから文字へ

#英小文字の判断方法？
#置換の関数は？
#import re
#re.sub(r'[a-z]+', 'xxx', src) # 'I xxx xxx.'

def cipher(x):
    return ''.join(chr(219-ord(c)) if 'a'<=c<='z' else c for c in x)

if __name__=="__main__":
	before = "My name is hogehoge33."
	after1 = cipher(before)
	after2 = cipher(after1)
	
print(before) 
print(after1) 
print(after2) 


