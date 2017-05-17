import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.isotonic import IsotonicRegression
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os
from os.path import basename

def draw_plot(filename):
    ds = pd.read_csv(filename, index_col=['Date'], parse_dates=['Date'])
    ds.as_matrix()
    plt = ds.plot(figsize=(12, 6))
    plt.get_figure().savefig("files/" + str(os.path.splitext(os.path.basename(filename))[0]) + "_origin.png")
    
def linreg(filename):
    ds = pd.read_csv(filename, names=["1", "2"], skiprows=1)
    ds["1"] = pd.to_datetime(ds["1"], format="%Y-%m")    
    ds["d"] = (ds["1"] - ds["1"].min())  / np.timedelta64(1,'D')

    X = ds["d"]  # put your dates in here
    y = ds["2"]  # put your kwh in here

    model = LinearRegression()
    model.fit(X.reshape(len(X), 1), y)

    X_predict = X  # put the dates of which you want to predict kwh here
    y_predict = model.predict(X_predict.reshape(len(X_predict), 1))
    fig = plt.figure(figsize=(12, 6))
    plt.plot(y)
    plt.plot(y_predict)
    fig.savefig("files/" + str(os.path.splitext(os.path.basename(filename))[0]) + "_linreg.png")

def isoreg(filename):
    ds = pd.read_csv(filename, names=["1", "2"], skiprows=1)
    ds["1"] = pd.to_datetime(ds["1"], format="%Y-%m")    
    ds["d"] = (ds["1"] - ds["1"].min())  / np.timedelta64(1,'D')

    X = ds["d"]  # put your dates in here
    y = ds["2"]  # put your kwh in here

    model =  IsotonicRegression()
    model.fit_transform(X, y)

    X_predict = ds["d"]  # put the dates of which you want to predict kwh here
    y_predict = model.predict(X_predict)
    fig = plt.figure(figsize=(12, 6))
    plt.plot(y)
    plt.plot(y_predict)
    fig.savefig("files/" + str(os.path.splitext(os.path.basename(filename))[0]) + "_isoreg.png")