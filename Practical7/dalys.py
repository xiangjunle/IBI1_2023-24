import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.iloc[0:101:10,3]

#used a Boolean to show DALYs for all rows corresponding to Afghanistan
my_columns = [False, False, False, True]
for i in range(0,6840):
    x=dalys_data.iloc[i,0]
    if x=="Afghanistan":
        dalys_data.iloc[i,my_columns]
#the DALYs in China in 2019 was less than the mean
china_data=dalys_data.iloc[1140:1170,0:5]

plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
