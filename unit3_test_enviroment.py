from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '../chromedriver'
init_script = "document.getElementsByClassName('runner-canvas')[0].id = 'runner-canvas'"

def save_obj(obj, name ):
    with open('objects/'+ name + '.pkl', 'wb') as f: #dump files into objects folder
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
def load_obj(name ):
    with open('objects/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
def grab_screen(_driver):
    image_b64 = _driver.execute_script(getbase64Script)
    screen = np.array(Image.open(BytesIO(base64.b64decode(image_b64))))
    image = process_img(screen)#processing image as required
    return image
def process_img(image):
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #RGB to Grey Scale
    image = image[:300, :500] #Crop Region of Interest(ROI)
    image = cv2.resize(image, (80,80))
    return  image
def show_img(graphs = False):
    """
    Show images in new window
    """
    while True:
        screen = (yield)
        window_title = "logs" if graphs else "game_play"
        cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)        
        imS = cv2.resize(screen, (800, 400)) 
        cv2.imshow(window_title, screen)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break

class Game:
    def __init__(self,custom_config=True):
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--mute-audio")
        self._driver = webdriver.Chrome(executable_path = chrome_driver_path,chrome_options=chrome_options)
        self._driver.set_window_position(x=-10,y=0)
        self._driver.get('chrome://dino')
        self._driver.execute_script("Runner.config.ACCELERATION=0")
        self._driver.execute_script(init_script)
    # 這邊用class function：
    def get_crashed(self): # 確定小恐龍有無因撞到障礙物結束遊戲
        return self._driver.execute_script("return Runner.instance_.crashed")
    def get_playing(self): # 確認在遊戲過程狀態中有無結束遊戲
        return self._driver.execute_script("return Runner.instance_.playing")
    def restart(self): # 重啟遊戲
        self._driver.execute_script("Runner.instance_.restart()")
    def press_up(self): # 往上跳躍
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
    def get_score(self): # 取得分數
        score_array = self._driver.execute_script("return Runner.instance_.distanceMeter.digits")
        score = ''.join(score_array) # the javascript object is of type array with score in the formate[1,0,0] which is 100.
        return int(score)
    def pause(self):  # 暫停
        return self._driver.execute_script("return Runner.instance_.stop()")
    def resume(self): # 重啟暫停狀態
        return self._driver.execute_script("return Runner.instance_.play()")
    def end(self): # 結束selenium
        self._driver.close()

class DinoAgent:
    def __init__(self,game): #takes game as input for taking actions
        self._game = game
        self.jump(); # 要先跳第一步，遊戲才能開始
    def is_running(self): 
        return self._game.get_playing()
    def is_crashed(self):
        return self._game.get_crashed()
    def jump(self):
        self._game.press_up()
    def duck(self): # 這邊有實作往下，但實際上我們不會用到，進階版如果有直撲而來的鳥就有需要了。
        self._game.press_down()

class Game_state:
    def __init__(self,agent,game):
        self._agent = agent
        self._game = game
        self._display = show_img() # 顯示小畫面
        self._display.__next__() # python語法，產生iter效果
    # 這邊先介紹要輸入的動作action，action[0]為不跳，action[1]為跳
    def get_state(self,actions):
        score = self._game.get_score() # 跟selenium要最新畫面
        reward = 0.1 # 先設定reward=0.1，只要能持續在場上皆會有0.1獎勵
        is_over = False # 遊戲是否結束
        if actions[1] == 1:  # 決定是否跳躍
            self._agent.jump()
            image = grab_screen(self._game._driver) # 圖像前處理，下章介紹
        self._display.send(image) # 傳送畫面到小視窗
        if self._agent.is_crashed(): # 確定是否結束
            self._game.restart() # 重新開啟
            reward = -1 # 給負獎懲
            is_over = True # 確認結束
        return image, reward, is_over #return the Experience tuple
    # get_state對照gym就是step，這裡也會回傳下個state、獎勵跟terminate。

game = Game()
dino = DinoAgent(game)
game_state = Game_state(dino,game) 

print('成功運行Game_state!')