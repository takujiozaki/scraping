#ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
#driver_path = 'drivers/chromedriver'
# ドライバーの自動インストール
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(executable_path=driver_path))

#ページ接続
driver.get('http://127.0.0.1:8000/')

#ページタイトルを取得
page_title = driver.title
print(page_title)


#グーを選ぶ
driver.find_element(By.ID,'playerRock').click()

#決定ボタンをクリック
driver.find_element(By.XPATH,'/html/body/div/div/div/form/div[2]/button').click()

time.sleep(1)

#移動先のタイトルを取得
page_title = driver.title
print(page_title)

#結果を取得
print(driver.find_element(By.CSS_SELECTOR,'.d-flex div:last-child > span').text)

time.sleep(1)

# クロームの終了処理
driver.close()

