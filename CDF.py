# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:31:30 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from pylab import mpl
from matplotlib.font_manager import FontProperties
#from pyecharts import Map, Geo
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements.""" 
    # Number of data points: n
    n = len(data) 
    # x-data for the ECDF: x
    x = np.sort(data) 
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n 
    return x, y




df = pd.read_csv('mangguo.csv',encoding='gbk')
df.head()
df.info()
df.describe()
x1 = df.loc[:,('Goods_Num','Monthly_Sales')]
x1 = np.array(x1)
s1 = list(x1[:,0])
s2 = list(x1[:,1])

x_std1,y_std1=ecdf(s1)
x_std2,y_std2=ecdf(s2)
plt.plot(x_std1,  y_std1,linestyle='-',linewidth=3, color='r',)
plt.plot(x_std2,  y_std2,linestyle='-.',linewidth=3, )
#plt.plot(x_std2,  y_std2,linestyle='-',linewidth=3, color='r',)

#plt.xlabel("收货数", fontproperties=font_set)
#plt.title('Tmall&Taobao CDF')
plt.ylabel("CDF")
plt.grid(True, linestyle="-")
plt.legend(('Goods','MSales'), loc='lower right')
#plt.legend(prop =font_set)
plt.xscale('log')
plt.ylim(0,1)
plt.xlim(xmin=0)
plt.margins(0.02)
plt.savefig("./data/shouhuo_xiaoshou.png")
plt.show()