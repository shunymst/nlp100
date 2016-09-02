

#-----------------------------------------------------------------------------------
#07. テンプレートによる文生成
#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

#引数の受け取り方 http://www.python-izm.com/contents/basis/command_line_arguments.shtml
#param[1] param[1] param[1]

import sys

param = sys.argv
time = param[1]
label = param[2]
temp = param[3]

print("★" + str(param[1]) + "時の" + str(param[2]) + "は" + str(param[3]))

