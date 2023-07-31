#ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver_path = 'drivers/chromedriver'
# ドライバーの自動インストール
# driver_path = ChromeDriverManager().install()
options = webdriver.ChromeOptions()
# ブラウザを起動しないオプション
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(executable_path=driver_path),options=options)

#ページ接続
driver.get('https://www.sozosha.ac.jp/')
#ページタイトルを取得
page_title = driver.title
print(page_title)
#aタグの要素を取得
h2_elements = driver.find_elements(By.TAG_NAME,'h2')
print("{}個のH2要素が見つかりました".format(len(h2_elements)))
for h2_element in h2_elements:
    print(h2_element.text) 
#クロームの終了処理
driver.close()

