import pandas as pd
import math as mt
import random as rand
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lecture des data
data = pd.read_csv('data/math0487_fa22_hw1_data.csv', usecols=[10])

meanAlcohol = data.mean()

biasMean = np.array([])
varMean = np.array([])


for i in range(1, 101):
    biasSampleLengthI = np.array([])
    meanSampleLenghtI = np.array([])
    for j in range(500):
        sample = data.sample(i)
        meanSample = sample.mean()
        biasSampleLengthI = np.append(biasSampleLengthI, abs(meanSample - meanAlcohol))
        meanSampleLenghtI = np.append(meanSampleLenghtI, meanSample)
    
    biasMean = np.append(biasMean, biasSampleLengthI.mean())
    varMean = np.append(varMean, meanSampleLenghtI.var())

        


plt.plot(biasMean)
plt.plot(varMean)
plt.legend(["bias of mean", "variance of mean"], loc ="upper right")
plt.show()

        

        



# calcul des valeurs demandées
...

# visualisation de la dataframe
