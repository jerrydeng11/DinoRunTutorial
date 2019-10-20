# Dino Run Tutorial

A Deep Convolutional Neural Network to play Google Chrome's offline Dino Run game by learning action patterns from visual input using a model-less Reinforcement Learning Algorithm

Accompanying code for Paperspace tutorial ["Build an AI to play Dino Run"](https://blog.paperspace.com/dino-run/)

<br><br/>

[![Video Sample](https://media.giphy.com/media/Ahh7X6z7jZSSl4veLf/giphy.gif)](http://www.youtube.com/watch?v=w1Rqf2oxcPU)

# Installation 
Start by cloning the repository
<br>
<br>
`$ git clone https://github.com/leeivan1007/DinoRunTutorial.git`
<br>
You need to initialize the file system to save progress and resume from last step.<br/>
Invoke `init_cache()` for the first time to do this <br/>


Dependencies can be installed using pip install or conda install for Anaconda environment

conda create -y resequet.yaml

## baselines

git clone https://github.com/openai/baselines/tree/master/baselines

cd baselines

pip install -e .

## chromedriver

至https://chromedriver.chromium.org/，選定穩定版本(Latest stable release)，接著選擇指定的系統版本。下載檔案後解壓縮至指定路徑。

- Python 3.6 Environment with ML libraries installed (numpy,pandas,keras,tensorflow etc)
- Selenium
- OpenCV

<br/>
