import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import datetime as dt
import pandas as pd

df = pd.read_csv('TB_burden_countries_2014-07-30.csv')

#df.drop(df.columns[0], axis=1)

df = df[df['year'] == 2012]#get only data of 2012
df_by_pop = df.sort(columns='e_pop_num', ascending=False)#sort df by population
print df_by_pop[:5]

#df_country_pop = df_by_pop[['country', 'e_pop_num']][:5]
df_country_pop = df_by_pop[['e_pop_num', 'country']][:5]
#df_country_pop.hist()
#show()
print '-'*30
print df_country_pop.count
print '-'*30
s_index = df_country_pop['country'].values
print 'index: '+str(s_index)

df_country_pop.columns = ['Population', 'country']

#ax = df_country_pop.plot(kind='bar', use_index=False, title='5 Most populous countries', legend=True, sharex=False)
ax = df_country_pop.plot(kind='bar', use_index=False, title='5 Most populous countries')
ax.set_xticklabels(s_index)

show()
fig = ax.get_figure()
fig.savefig("Population_bars.pdf")



df_country_pop.plot(kind='pie', subplots=True)#works


show()
