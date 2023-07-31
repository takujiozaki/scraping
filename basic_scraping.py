#ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver_path = 'drivers/chromedriver'
# ドライバーの自動インストール
# driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(executable_path=driver_path))

#ページ接続
driver.get('https://www.sozosha.ac.jp/')
#キー入力

#クロームの終了処理
driver.close()

