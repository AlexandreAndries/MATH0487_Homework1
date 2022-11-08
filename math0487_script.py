import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
# ...

# visualisation de la dataframe
print(df_q1_1)
