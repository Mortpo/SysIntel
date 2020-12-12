import numpy as np
import keras.backend as K
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import csv
import matplotlib.pyplot as plt

data=[]
truedata=[]
with open('DataTest.csv', newline='') as csvdata:
    datareader = csv.reader(csvdata, delimiter=',')
    datareader.__next__()
    i = 0
    for row in datareader:
        i+=1
        if i<30:
            data.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6])])
            truedata.append([int(row[7])])

v_x=np.asarray(data)
v_x=np.reshape(v_x,(len(v_x),1,7))
v_y=keras.utils.to_categorical(truedata)
v_y=np.reshape(v_y,(len(v_y),1,10))

model = keras.models.load_model('best.h5')


predictions = model.predict_on_batch(v_x)
k=0
for i in predictions:
    for j in i:

            plt.plot(j)
            b=[]
            for a in range(10):
                b.append(v_y[k][0][a])
            print(b)
            plt.plot(b)
            plt.title('Prediction')
            plt.ylabel('Confiance')
            plt.xlabel('Valeur 0 à 9')
            plt.legend(['Prediction', 'Valeur'], loc='upper left')
            plt.show()
            k+=1



#print(round([v[0] for v in predictions]))