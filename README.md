# Dino Run Tutorial

小恐龍訓練+Q-learnin實作，詳情請參考[人工智慧(RL系列) 完爆遊戲30天系列文章](https://ithelp.ithome.com.tw/users/20121110/ironman/2855)
想直接嘗試小恐龍訓練，請完成下面**下載與環境建置**、**baselines安裝**、**chromedriver安裝**後直接執行
```
python unit5_dino.py
```
訓練過程隨時可按ctrl+c結束訓練，下次的訓練仍然會使用過去的模型與搜集的樣本。
如在pickle發生object的error請參考下方的**object_error**

[![Video Sample](https://media.giphy.com/media/Ahh7X6z7jZSSl4veLf/giphy.gif)](http://www.youtube.com/watch?v=w1Rqf2oxcPU)

# 下載與環境建置
```git clone https://github.com/leeivan1007/DinoRunTutorial.git
cd DinoRunTutorial
conda env create --file environment.yaml
source activate dino_rl
```
## baselines安裝
Open_AI reinforcement learning算法
```
git clone https://github.com/openai/baselines/tree/master/baselines
cd baselines
pip install -e .
```
## chromedriver安裝

至[https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)，選定穩定版本(Latest stable release)，接著選擇指定的系統版本。下載檔案後解壓縮至指定路徑。

如果是照著專案的指示，那你的chromdriver路徑要放在專案的上一層

root_home/

         chromedriver
         
         DinoRunTutorial

或在py檔案裡面修改變數(chrome_driver_path)的路徑。

## object_error

如果出現pickle讀取objects的物件出現異常，或想重新把過去的訓練檔案消除，請執行
```
python clear_objects.py 
```

## 原文參考

Accompanying code for Paperspace tutorial ["Build an AI to play Dino Run"](https://blog.paperspace.com/dino-run/)