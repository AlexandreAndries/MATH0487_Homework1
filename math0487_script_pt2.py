import pandas as pd
import math as mt
import random as rand
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lecture des data
data = pd.read_csv('data/math0487_fa22_hw1_data.csv', usecols=[10])

#Premier graphique
meanAlcohol = data.mean()
varAlcohol = data.var()

biasMean = np.array([])
biasVar = np.array([])


varMean = np.array([])
varVar = np.array([])

for i in range(1, 101):
    biasMeanSample = np.array([])
    biasVarSample = np.array([])
    varSamples = np.array([])
    meanSamples = np.array([])
    for j in range(500):
        sample = data.sample(i)
        meanSample = sample.mean()
        varSample = sample.var()

        biasMeanSample = np.append(biasMeanSample, abs(meanSample - meanAlcohol))
        biasVarSample = np.append(biasVarSample, abs(varSample - varAlcohol))

        varSamples = np.append(varSamples, varSample)
        meanSamples = np.append(meanSamples, meanSample)
    

    biasVar = np.append(biasVar, biasVarSample.var())
    biasMean = np.append(biasMean, biasMeanSample.mean())
    varVar = np.append(varVar, varSample.var())
    varMean = np.append(varMean, meanSamples.var())

        


figure, axis = plt.subplots(1, 2)

axis[0].plot(biasMean)
axis[0].plot(varMean)
axis[0].set_title("2.1.a")
axis[0].legend(["biais de la moyenne", "variance de la moyenne"] , loc = "upper right")

axis[1].plot(biasVar)
axis[1].plot(varVar)
axis[1].set_title("2.1.b")
axis[1].legend(["biais de la variance", "variance de la variance"] , loc = "upper right")


plt.show()
