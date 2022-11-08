import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Q1.1 =========================================================================
# initialisation de la dataframe (à remplir)
idx = ['10th', '20th', '30th']
var = ['fixed acidity', 'pH', 'alcohol']
df_q1_1 = pd.DataFrame(np.zeros((3,3)), idx, var)
df_q1_1

# chargement du dataset
data = pd.read_csv('data/math0487_fa22_hw1_data.csv') #
df_q1_1 = pd.DataFrame(data, index=[9,19,29], columns=var) #
df_q1_1.index = idx

# calcul des valeurs demandées
# Mean -----
means = df_q1_1.mean()

# Median -----
medians = df_q1_1.median()

# Std Dev -----
stdDevs = df_q1_1.std()

# visualisation de la dataframe
print(df_q1_1) #

# Q1.2 =========================================================================
# initialisation de la dataframe (à remplir)
var = ['fixed acidity', 'pH', 'alcohol']
idx = ['mean', 'std', 'median', 'q25', 'q75']
df_q1_2 = pd.DataFrame(np.zeros((5,3)), idx, var)

# calcul des valeurs demandées
...

# visualisation de la dataframe
print(df_q1_2)
