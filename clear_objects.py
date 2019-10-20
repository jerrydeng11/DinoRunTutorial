import pickle
from collections import deque

def save_obj(obj, name ):
    with open('objects/'+ name + '.pkl', 'wb') as f: #dump files into objects folder
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

save_obj(0.1,"epsilon")
t = 0
save_obj(t,"time")
D = deque()
save_obj(D,"D")
