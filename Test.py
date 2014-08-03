import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import datetime as dt
import pandas as pd

df = pd.read_csv('TB_burden_countries_2014-07-30.csv')

df_ger = df[df['country'] == 'Germany']
df_ger12 = df_ger[df_ger['year'] == 2012]
print df_ger12

#get the population of each year
series_pop = df_ger['e_pop_num']

ls_values = series_pop.values

#series = pd.Series(data = ls_values, index=pd.date_range('1/1/2000', periods=23))
series = pd.Series(data = ls_values, name='Population', index=pd.date_range(start='1990', periods=23, freq='A' , name='Years'))

series.plot()
show()