#外部ライブラリを必ずインストールする
#pip install requests

import requests
r = requests.get("https://www.sozosha.ac.jp/")
print(type(r))
print("status code:{}".format(r.status_code))
print("encoding:{}".format(r.encoding))
print("text:{}".format(r.text))
