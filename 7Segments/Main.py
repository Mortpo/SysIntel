import numpy as np
import keras.backend as K
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import csv

data=[]
truedata=[]
with open('data.csv', newline='') as csvdata:
    datareader = csv.reader(csvdata, delimiter=',')
    datareader.__next__()
    for row in datareader:
        data.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6])])
        truedata.append([int(row[7])])

x=np.asarray(data)
x=np.reshape(x,(9,1,7))
y=keras.utils.to_categorical(truedata)
y=np.reshape(y,(9,1,10))


data=[]
truedata=[]
with open('DataTest.csv', newline='') as csvdata:
    datareader = csv.reader(csvdata, delimiter=',')
    datareader.__next__()
    for row in datareader:
        data.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6])])
        truedata.append([int(row[7])])
v_x=np.asarray(data)
v_x=np.reshape(v_x,(len(v_x),1,7))
v_y=keras.utils.to_categorical(truedata)
v_y=np.reshape(v_y,(len(v_y),1,10))


sgd=SGD(learning_rate=0.3)

model = Sequential()
model.add(Dense(7,input_dim=7,activation='relu'))
model.add(Dense(16,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()
model.compile(optimizer=sgd, loss='categorical_crossentropy',metrics=[keras.metrics.CategoricalAccuracy()]) 
es = keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=0, patience=500)
mc = keras.callbacks.ModelCheckpoint('best.h5', monitor='val_loss', mode='min', verbose=0, save_best_only=True)
history=model.fit(x, y, epochs=500 , validation_data=(v_x,v_y),verbose=1, callbacks=[es,mc])



# summarize history for accuracy
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()