
import os
import numpy as np
import pandas as pd
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt


def scatterplot(x,y, title, xlabel, ylabel, save_path):
    plt.close()
    plt.figure(figsize=(10,8))
    plt.scatter(x,y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(save_path)

def correl(frame, point):
    for (column, data) in frame.iteritems():
        if(column != point):
            correlation = np.correlate(frame[point], data)
            if not os.path.exists("../graphs/" + point):
                os.makedirs("../graphs/" + point)
            scatterplot(frame[point], data, str(correlation), point, column, "../graphs/" + point + "/" + column + ".png")


def filter_dep():
    frame = pd.read_csv("../screenTime/maps-synthetic-data-v1.1.csv", index_col=0)

    frame = frame[pd.notnull(frame['has_dep_diag'])]
    frame['has_dep_diag'] = frame['has_dep_diag'].map({" No ICD-10 diagnosis of depression": 0, "Yes ICD-10 diagnosis of depression":1})
    frame = frame.drop(['X', 'flag'], axis=1)
    print(frame['has_dep_diag'])
    frame.to_csv("has_dep_diag_filt.csv")
    return frame

if __name__ == "__main__":
    #frame = filter_dep()
    frame = pd.read_csv("has_dep_diag_filt.csv", index_col=0)

    frame = frame.select_dtypes(include='number')

    for(column, data) in frame.iteritems():
        correl(frame,column)
