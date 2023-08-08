#ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#driver_path = 'drivers/chromedriver'
# ドライバーの自動インストール
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(executable_path=driver_path))

#ページ接続
driver.get('http://127.0.0.1:5500/')

#ページタイトルを取得
page_title = driver.title
print(page_title)

# タグの取得(単一)
h1_element = driver.find_element(By.TAG_NAME,'h1')
print(h1_element.text)

# タグの取得(複数)
h2_elements = driver.find_elements(By.TAG_NAME,'h2')
for h2_element in h2_elements:
    print(h2_element.text)

# クラスの取得
class_elements = driver.find_elements(By.CLASS_NAME,'card-body')
for class_element in class_elements:
    print(class_element.text)

# CSSセレクター
css_selector = driver.find_element(By.CSS_SELECTOR,'body > div > div:nth-child(3) > div.card-body')
print(css_selector.text)

# XPath
x_path = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]')
print(x_path.text)
# クロームの終了処理
driver.close()

