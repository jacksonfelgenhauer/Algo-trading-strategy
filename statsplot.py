#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Stats():
    def __init__(self,ticker,start,end):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.get_data()
        
    def get_data(self):
        df = yf.download(self.ticker, start = self.start, end = self.end, ignore_tz = True)
        close = df.loc[:,"Close"].dropna().copy()
        normclose = close.div(close.iloc[0]).mul(100)
        self.close2 = close
        self.normclose2 = normclose
        
        return close
        return normclose
    
    def normplot(self):
        self.normclose2.plot(figsize = (15,8), fontsize = 12)
        plt.legend(fontsize = 12)
        plt.show()
    
    def RRplot(self):
        ret = self.close2.pct_change().dropna()
        summary = ret.describe().T.loc[:,["mean", "std"]]
        summary["mean"] = summary["mean"]*252
        summary["std"] = summary["std"]*np.sqrt(252)
        summary.plot.scatter(x="std", y = "mean", figsize = (12,8), s= 50, fontsize =15) 
    
        for i in summary.index:
            plt.annotate(i, xy=(summary.loc[i,"std"]+0.002,summary.loc[i,"mean"]+0.002),size=11)
        plt.xlabel("Annual risk(std)", fontsize = 15)
        plt.ylabel("Annual return", fontsize = 15)
        plt.title("Risk/return", fontsize = 25)
        
    def corrplot(self):
        ret = self.close2.pct_change().dropna()
        ret.cov()
        ret.corr()
        
        plt.figure(figsize = (16,12))
        sns.set(font_scale=1.4)
        sns.heatmap(ret.corr(), cmap = "Reds", annot = True, annot_kws={"size":15},vmax=1)
        plt.show()

