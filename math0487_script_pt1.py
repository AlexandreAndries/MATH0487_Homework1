import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_diagram(df, title, ylab):

    fig, axes = plt.subplots(1)

    axes.set_title(title)
    axes.set(ylabel=ylab)
    axes.set_facecolor('azure')  # --> light blue background

    df.plot(kind='box')
    plt.tight_layout()
    plt.show()


def plot_histogram(df, title, ylab, xlab):
    fig, axes = plt.subplots(1)

    axes.set_title(title)
    axes.set(ylabel=ylab, xlabel=xlab)
    axes.set_facecolor('azure')  # --> light blue background

    plt.hist(df)
    plt.tight_layout()
    plt.show()


def plot_cdf(df, title, xlab):
    fig, axes = plt.subplots(1)

    # Frequency
    df = pd.DataFrame(df)
    df.rename(columns= {title:'value'}, inplace = True)
    dfFreq = df.sort_values(by=['value'])
    dfFreq = df.groupby('value')['value'].agg('count').pipe(pd.DataFrame).rename(columns={'value' : 'frequency'})

    # PDF
    dfFreq['pdf'] = dfFreq['frequency'] / sum(dfFreq['frequency'])

    # CDF
    dfFreq['cdf'] = dfFreq['pdf'].cumsum()
    dfFreq = dfFreq.reset_index()

    plt.plot(dfFreq['value'],dfFreq['cdf'], 'r')

    axes.set_title(title + " CDF")
    axes.set(xlabel=xlab, ylabel='Probability')
    axes.set_facecolor('azure')
    plt.tight_layout()
    plt.show()

def plot_cloud(x, y, title, xlab, ylab):
    fig, axes = plt.subplots(1)

    plt.plot(x,y,'ro')

    axes.set_title(title)
    axes.set(xlabel=xlab, ylabel=ylab)
    axes.set_facecolor('azure')
    plt.tight_layout()
    plt.show()

# Q1.1 =========================================================================
# initialisation de la dataframe (à remplir)
idx = ['10th', '20th', '30th']
var = ['fixed acidity', 'pH', 'alcohol']
df_q1_1 = pd.DataFrame(np.zeros((3, 3)), idx, var)
df_q1_1

# chargement du dataset
data = pd.read_csv('data/math0487_fa22_hw1_data.csv')
df_q1_1 = pd.DataFrame(data, index=[9, 19, 29], columns=var)
df_q1_1.index = idx

# calcul des valeurs demandées
# Mean -----
means = df_q1_1.mean()

# Median -----
medians = df_q1_1.median()

# Std Dev -----
stdDevs = df_q1_1.std()

# visualisation de la dataframe
print(df_q1_1)

# Q1.2 =========================================================================
# initialisation de la dataframe (à remplir)
var = ['fixed acidity', 'pH', 'alcohol']
idx = ['mean', 'std', 'median', 'q25', 'q75']
df_q1_2 = pd.DataFrame(np.zeros((5, 3)), idx, var)

# calcul des valeurs demandées
fullDF = pd.DataFrame(data, columns=var)
df_q1_2.loc["mean"] = fullDF.mean()
df_q1_2.loc["std"] = fullDF.std()
df_q1_2.loc["median"] = fullDF.median()
df_q1_2.loc["q25"] = fullDF.quantile(q=0.25)
df_q1_2.loc["q75"] = fullDF.quantile(q=0.75)

# # visualisation de la dataframe
print(df_q1_2)

# boites à moustaches
plot_diagram(fullDF['fixed acidity'], 'fixed acidity boxplot', 'g/dm^3')
plot_diagram(fullDF['pH'], 'pH boxplot', '-')
plot_diagram(fullDF['alcohol'], 'alcohol boxplot', 'vol%')

# histogrammes
plot_histogram(fullDF['fixed acidity'],
               'fixed acidity histogram', 'effectifs', 'g/dm^3')
plot_histogram(fullDF['pH'], 'pH histogram', 'effectifs', '-')
plot_histogram(fullDF['alcohol'], 'alcohol histogram', 'effectifs', 'vol%')

# cdf
plot_cdf(fullDF['fixed acidity'],
               'fixed acidity', 'g/dm^3')
plot_cdf(fullDF['pH'], 'pH', '-')
plot_cdf(fullDF['alcohol'], 'alcohol', 'vol%')

# Q1.3 =========================================================================
# comparaison numérique
df = pd.read_csv('data/math0487_fa22_hw1_data.csv', usecols=var)
rel_df = df.corr()

# visualisation
print(rel_df)

# comparaison graphique
plot_cloud(df['fixed acidity'], df['pH'], 'pH versus fixed acidity - Cloud', 'fixed acidity (g/dm^3)', 'pH (-)')
plot_cloud(df['fixed acidity'], df['alcohol'], 'alcohol versus fixed acidity - Cloud', 'fixed acidity (g/dm^3)', 'alcohol (vol%)')
plot_cloud(df['pH'], df['alcohol'], 'alcohol versus pH - Cloud', 'pH (-)', 'alcohol (vol%)')
