import random
import gym
env = gym.make('MountainCar-v0')
env.reset()
print('開始進行遊戲')
print('終機端按ctrl-c則可結束遊戲')
random_number = lambda:random.randint(0,2)

while True:
    env.step(random_number())
    env.render()
