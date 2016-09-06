#-----------------------------------------------------------------------------------
#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
#問題21-29では，ここで抽出した記事本文に対して実行せよ．

#JSON読み込み
jsonFile = 'jawiki-country.json'
import json

#f = open(jsonFile)
#data = json.load(f)
#print data["title"]

def getUK():
    with open(jsonFile) as f:
        json_data = f.readline()
        while json_data:
            article_dict = json.loads(json_data)
            if article_dict["title"] == u"イギリス":
                return article_dict["text"]
            else:
                json_data = f.readline()
    return ""
        	        
if __name__=="__main__":
	print("模範解答-------------------")
	with open(jsonFile) as f:#ファイル読み込み
	    article_json = f.readline()
	    while article_json: #順に取り出し
	        article_dict = json.loads(article_json) #
	        if article_dict["title"] == u"イギリス":
	            print(article_dict["text"])
	        article_json = f.readline()



