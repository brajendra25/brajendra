# imports for reading data from Yahoo!
from pandas_datareader import data, wb

from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd

print(pd.__version__)
'''
# read the last three months of data for GOOG
goog =data.DataReader("ebix", "yahoo",
date.today() +
relativedelta(years=-5))
goog.to_csv("Ebix_Share_price.csv")
print(goog.tail(10))

'''

df = pd.read_csv("Ebix_Share_price.csv")
nullCount = df.isnull().sum()
newdf = df.fillna(" ")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

df_2014 = df[df['Year'] == 2014]
print(df_2014)

