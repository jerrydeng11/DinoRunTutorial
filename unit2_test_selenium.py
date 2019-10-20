from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '../chromedriver' # 設定chromedriver路徑
init_script = "document.getElementsByClassName('runner-canvas')[0].id = 'runner-canvas'" # 元素設id
chrome_options = Options()
chrome_options.add_argument("--mute-audio") # 取消音效
driver = webdriver.Chrome(executable_path = chrome_driver_path,chrome_options=chrome_options) # 載入設定
driver.set_window_position(x=-10,y=0) # 設置視窗大小

driver.get('chrome://dino') # 進入網頁
driver.execute_script("Runner.config.ACCELERATION=0") # 禁止加速度
driver.execute_script(init_script) # 執行javascript語法

print('成功運行dino!')
