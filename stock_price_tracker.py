#!/usr/bin/env python
# coding: utf-8

# ### Import modules

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from PIL import Image
import yfinance as yf


# ### User selects three stocks to track

# In[ ]:


ticker_list = []

for i in range(1, 4):
    ticker_list.append(input('Enter stock number ' + str(i) + ' to track: '))


# ### Collect data from past 5 years for selected stocks

# In[ ]:


tickers = str(ticker_list[0] + ' ' + ticker_list[1] + ' ' + ticker_list[2])
 
yahoo_data = yf.download(tickers = tickers,
                         period = '5y',
                         interval = '1d',
                         group_by = 'ticker')


# ### Organize data into a tidy dataframe for plotting

# In[ ]:


df = (yahoo_data
          .filter(items = [(ticker_list[0], 'Close'), (ticker_list[1], 'Close'), (ticker_list[2], 'Close')])
          .reset_index()
          .droplevel(1, axis = 1)
          .melt(id_vars = ['Date'], value_vars = ticker_list, var_name = 'Ticker', value_name = 'Price')
          .query('Price == Price')
          .reset_index(drop = True))


# ### Create plot

# In[ ]:


plt.figure(figsize = (20, 10))

plt.plot(df[df['Ticker'] == ticker_list[0]]['Date'],
         df[df['Ticker'] == ticker_list[0]]['Price'],
         label = ticker_list[0])

plt.plot(df[df['Ticker'] == ticker_list[1]]['Date'],
         df[df['Ticker'] == ticker_list[1]]['Price'],
         label = ticker_list[1])

plt.plot(df[df['Ticker'] == ticker_list[2]]['Date'],
         df[df['Ticker'] == ticker_list[2]]['Price'],
         label = ticker_list[2])

plt.title('Stock Prices over the Last Five Years')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Closing Price')

fname = str(ticker_list[0] + '_' + ticker_list[1] + '_' + ticker_list[2] + '.png')

plt.savefig(fname = fname)


# ### Open and display plot

# In[ ]:


img = Image.open(fname)
img.show()

