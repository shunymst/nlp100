#-----------------------------------------------------------------------------------
#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

#国旗画像': 'Flag of the United Kingdom.svg
gazou="Flag of the United Kingdom.svg"

import re
import requests

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict
    
url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           #"titles": "File:{}".format(temp_dict[u"国旗画像"]),
           "titles": "File:{}".format(gazou),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()

print(json_search(json_data)["url"])
