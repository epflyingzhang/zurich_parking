# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:12:42 2020

@author: Ying
"""

# project plan - City Parking in Zurich explained
# --------------------
# Goals:
# - Visualize street parking + parking house location + postalcode geojson 
#   - Find free parking or 15h parking white zone, visualize on map -> practice Plotly Map
#   - blue zones by ZIP code, visualize on map
#   - add white zone, free parking overnight (if you arrive in the evening and leave early morning)
# ----- publish first version
#   - if you would like to park longer in the city, visualize park house (by )
#   - if you have a lot of money, and do not mind parking overnight in park house
# - Some EDA, draw some conclusion 
# - build a forecasting model (hourly) of parking availability 
# --------------------
# Data gathering:
# 1. ask for historical parking availability data
# 2. if not available, load XML file online -> for at least one week
# --------------------
#
# Other ideas:
# --------------------
# street parking location
# parkding lot data
# weather data?
# public holiday data?

# we can scrap opening time, number, price from this website: https://www.pls-zh.ch/parkhaus/accu.jsp?pid=accu
# get real time parking space data from (XML): https://www.pls-zh.ch/plsFeed/rss
# https://www.parkme.com/en-gb/zurich-ch-parking 


import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.getcwd()
os.listdir('data/')


df_sp = pd.read_csv('data/zuri_street_pp.csv')

# first look at street parking data
df_sp.info()

df_sp['art'].value_counts()
df_sp['gebuehrenpflichtig'].value_counts()
df_sp['parkdauer'].value_counts()

sns.countplot('art', hue='gebuehrenpflichtig', data=df_sp)

%matplotlib qt5
sns.barplot(x=df_sp['parkdauer'].value_counts().index, y=df_sp['parkdauer'].value_counts().values)
#%matplotlib inline

# geojson
import shapefile
from json import dumps

reader = shapefile.Reader("data/PLZO_SHP_LV03_ZIP_shape_files/PLZO_PLZ.shp")

# read the shapefile
fields = reader.fields[1:]
field_names = [field[0] for field in fields]

buffer = []
for sr in reader.shapeRecords():
   atr = dict(zip(field_names, sr.record))
   geom = sr.shape.__geo_interface__
   buffer.append(dict(type="Feature", geometry=geom, properties=atr)) 

print(len(buffer), buffer[0].keys(), buffer[0]['properties']['PLZ'])

# --> voila. seems we got the geojson data of PLZ shapes

