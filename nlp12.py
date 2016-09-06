#================================================================================
#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
txt = "hightemp.txt"
import subprocess

#列の抜出の仕方
#ダイレクトにN列目を抜き出すというものはないので読み込んで、空白からN個め　で取得
#http://qiita.com/Ria0130/items/7573302aa48edfe94c36
#mode はオプションの文字列で、ファイルが開かれるモードを指定します。
#デフォルトは 'r' で、読み込み用にテキストモードで開くという意味です。
#その他のよく使われる値は、書き込み (ファイルがすでに存在する場合はそのファイルを切り詰めます) 用の ★'w'、排他的な生成用の 'x'、追記用の 'a' です
r = open(txt).readlines()
with open('col1.txt', 'w') as c1, open('col2.txt', 'w') as c2:
    for l in r:
        s = l.split('\t')
        c1.write(s[0]+'\n')
        c2.write(s[1]+'\n')


print("コマンドで確認")
#cut -f1 hightemp.txt
subprocess.call( ["cut", "-f1", txt] ) 
subprocess.call( ["cut", "-f2", txt] ) 



