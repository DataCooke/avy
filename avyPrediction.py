import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max.columns", None)

avy = pd.read_csv("avalanches1_9_2020.csv")

avy['Elevation'] = avy['Elevation'].str.replace(r'\'', '')
avy['Elevation'] = avy['Elevation'].str.replace(r',', '')
avy['Elevation'] = pd.to_numeric(avy['Elevation'])

avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "North"),'location']='North 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "Northeast"),'location']='NorthEast 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "East"),'location']='East 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "Southeast"),'location']='SouthEast 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "South"),'location']='South 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "Southwest"),'location']='SouthWest 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "West"),'location']='West 9500+'
avy.loc[(avy.Elevation >= 9500) & (avy.Aspect == "Northwest"),'location']='NorthWest 9500+'

avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "North"),'location']='North 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "Northeast"),'location']='NorthEast 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "East"),'location']='East 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "Southeast"),'location']='SouthEast 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "South"),'location']='South 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "Southwest"),'location']='SouthWest 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "West"),'location']='West 8k-9500'
avy.loc[(avy['Elevation'].between(8000, 9499)) & (avy.Aspect == "Northwest"),'location']='NorthWest 8k-9500'

avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "North"),'location']='North <8000>'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "Northeast"),'location']='Northeast <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "East"),'location']='East <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "Southeast"),'location']='SouthEast <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "South"),'location']='South <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "Southwest"),'location']='SouthWest <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "West"),'location']='West <8000'
avy.loc[(avy.Elevation < 8000) & (avy.Aspect == "Northwest"),'location']='NorthWest <8000'

avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
avyN9500 = avy[avy['location'] == 'North 9500+']
#df_new = df[df['Pid'] == 'p01']
print("avyN9500 below")
print(avyN9500)


'''
def label_location (row):
   if row['Elevation'] > 9500 & row['Aspect'] == "North" :
      row['location'] 'North 9500+'
    row['location'] "na"

avy.apply(lambda row: label_location(row), axis=1)
'''
print(avy.loc[avy['location'] == 'North 8k-9500'])
print(avy.head())

avy['Elevation'] = avy['Elevation'].str.replace(',', '')
avy['Elevation'] = avy['Elevation'].str.replace("'", "")
avy["Elevation"] = pd.to_numeric(avy["Elevation"])
avy['+9500'] = ''
avy['8000-9500'] = ''
avy['Below 8000'] = ''
avy['Alt'] = ''
avy.loc[avy['Elevation'] > 9500, '+9500'] = '1'
avy.loc[avy['Elevation'].between(8000, 9500), '8000-9500'] = '1'
avy.loc[avy['Elevation'] < 8000, 'Below 8000'] = '1'
avy.loc[avy['Elevation'] > 9500, 'Alt'] = 'High'
avy.loc[avy['Elevation'].between(8000, 9500), 'Alt'] = 'Mid'
avy.loc[avy['Elevation'] < 8000, 'Alt'] = 'Low'
avy = avy[avy.Alt != '']
print(avy.head())

avy = pd.DataFrame(avy)
avySubset = avy.groupby(['Date']).size().reset_index()
avySubset.columns = ['Date', 'Avalanches']
#avySubset = pd.DataFrame(avySubset)
avySubset.head()

avySubset["Date"] = pd.to_datetime(avySubset["Date"])
avySubset = avySubset.sort_values(by="Date")
avySubset = avySubset[avySubset['Date'] > '2018-09-01'].reset_index().drop(['index'], axis = 1)
avySubset =  avySubset[(avySubset['Date'] < '2019-05-31') | (avySubset['Date'] > '2019-09-01')].reset_index().drop(['index'], axis = 1)
print(avySubset)

idx = pd.date_range(avySubset['Date'].min(), avySubset['Date'].max())
avySubset.index = avySubset['Date']
avySubset = avySubset.reindex(idx, fill_value=0)
avySubset = avySubset.drop(columns=['Date']).reset_index()
avySubset.columns = ['Date', 'Avalanches']
print(avySubset)

from datetime import datetime
from datetime import timedelta

startDate = '2020-02-02'

startDate = datetime.strptime(startDate, '%Y-%m-%d')
endDate = startDate + timedelta(days=1)

startDate = str(startDate)
endDate = str(endDate)

import http.client
import os

conn = http.client.HTTPSConnection("dark-sky.p.rapidapi.com")
secret_key = os.environ.get('weather_api_key')

headers = {
    'x-rapidapi-host': "dark-sky.p.rapidapi.com",
    'x-rapidapi-key': secret_key
    }

conn.request("GET", "/40.600749,-111.637541,1577836800", headers=headers)

res = conn.getresponse()
data = res.read()


print(data.decode("utf-8"))

import json
r = json.loads(data)
r["daily"]

'''
import json
r = json.loads(data)
r["daily"]["data"][0]["summary"]

startDates = ['2020-02-02','2020-02-03']
endDates = ['2020-02-03','2020-02-04']
startDates = [datetime.strptime(date, '"%Y-%m-%d"') for date in startDates]
endDates = [datetime.strptime(date, '"%Y-%m-%d"') for date in endDates]


base = datetime.datetime.today()
dates = [base - datetime.timedelta(days=5) for x in range(numdays)]



#for i in dates
#print(i)

import pandas as pd

start = datetime.datetime(2020, 1, 2)

datelist = pd.date_range(start, periods=4).strftime("%Y-%m-%d").tolist()
print(datelist)
'''