from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD , Adam
from keras.callbacks import TensorBoard



model = Sequential()
model.add(Conv2D(32, (8, 8), padding='same',strides=(4, 4),input_shape=(80,80,4)))  #80*80*4
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))
model.add(Conv2D(64, (4, 4),strides=(2, 2),  padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3),strides=(1, 1),  padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dense(2))
adam = Adam(lr=1e-4)
model.compile(loss='mse',optimizer=adam)

print(model.summary())