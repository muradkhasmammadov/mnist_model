from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import  Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
from keras.utils import np_utils
import matplotlib.pyplot as plt

batch_size = 128
num_classes = 10
epochs = 10

#data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# plt.imshow(x_train[59999])

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

#convert class vectors to binary matrixes

y_train = keras.utils.np_utils.to_categorical(y_train, num_classes)
y_test = keras.utils.np_utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(784, activation = 'relu', input_shape = (784,)))
model.add(Dropout(0.2))
model.add(Dense(392, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation = 'softmax'))
model.summary()

model.compile(loss = 'categorical_crossentropy',
              optimizer = RMSprop(),
              metrics = ['accuracy'])

history = model.fit(x_train, y_train, 
                    batch_size = batch_size,
                    epochs = epochs,
                    verbose = 1,
                    validation_data = (x_test, y_test))

score = model.evaluate(x_test, y_test)
print('Test Loss: ', score[0])
print('Test Accuracy: ', score[1])

from keras.models import load_model

model.save('Desktop\mnist_model.h5')

prediction_test_data = model.predict(x_test)
plt.plot(prediction_test_data, 'o')
