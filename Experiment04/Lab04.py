#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""implement the data processing, data visualization and data wrangling on any real-world problem i.e 
covid_19 dataset to view the active cases on the world map using chloropleth and also plot the cases."""


# In[2]:


pip install folium


# In[8]:


import folium as flm
from folium import plugins
import pandas as pd
import json
import requests


# In[9]:


#loading geo-JSON data
with open(r"C:/Users/HP/Downloads/Indian_States.json") as f:
    geojson_states = json.load(f)


# In[10]:


#assigning name of states to a key called 'id'
for i in geojson_states['features']:
    i['id'] = i['properties']['NAME_1']


# In[11]:


#requesting data from api
res = requests.get('https://api.covid19india.org/data.json')
covid_current = res.json()
df = []


# In[13]:


#filtering data for a better understanding
for j in range(1, 37):
    if(covid_current['statewise'][j]['state'] != 'State Unassigned'):
        df.append([covid_current['statewise'][j]['state'],
                covid_current['statewise'][j]['confirmed'],
                covid_current['statewise'][j]['active'],
                covid_current['statewise'][j]['deaths'],
                ])
        df_covid = pd.DataFrame(df, columns=['State', 'Total Case', 'Active Case', 'Deaths'])

df_covid.head(50)


# In[14]:


#filtering the fetched data
df_covid = df_covid.sort_values('State', axis = 0)
df_covid = df_covid.reset_index(drop=True)

df_covid['State'].iloc[7] = 'Dadra and Nagar Haveli'
df_covid.head(10)


# In[17]:


#Exporting data to a CSV file
df_covid.to_csv('TotalCase.csv')


# In[18]:


#Reading CSV file for easier references
pop_df = pd.read_csv('TotalCase.csv')


# In[19]:


#Adding fetched data from API to Geo-JSON file for later use
for i in range(35):
    if((geojson_states['features'][i]['properties']['NAME_1']) == (df_covid['State'][i])):
        geojson_states['features'][i]['properties']['total_case'] = df_covid['Total Case'][i]
        geojson_states['features'][i]['properties']['active_case'] = df_covid['Active Case'][i]
        geojson_states['features'][i]['properties']['total_deaths'] = df_covid['Deaths'][i]     


# In[20]:


#Creating a Folium Map Object
# Replace "YOUR_MAPBOX_TOKEN" with your actual Mapbox access token
map1 = flm.Map(location=[20.5937,78.9629], zoom_start=4, tiles='https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2F1cmFiaDIxMDUiLCJhIjoiY2xnMzJ0ZHE3MDV3ODNnbW4zazJ5YTVxZSJ9.SHzd_4oZyjvw0xxxh-kB3w', attr='Mapbox Bright')

# Add a marker to the map
flm.Marker([20.5937,78.9629], popup='India').add_to(map1)

# Display the map
map1


# In[21]:


#Adding more tiles to the map
tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
for tile in tiles:
    flm.TileLayer(tile).add_to(map1)


# In[22]:


#Providing required data to the map for plotting
choropleth = flm.Choropleth(
    geo_data=geojson_states,
    name='Total Case',
    data=pop_df,
    columns=['State', 'Total Case'],
    key_on='feature.id',
    fill_color='Set2',
    fill_opacity=0.5,
    line_opacity=0.5,
    nan_fill_color='white',
    nan_fill_opacity=1, 
    line_weight=0.8,
    highlight=True,
    legend_name='State-wise COVID-19 Cases in INDIA',
	reset=True
    ).add_to(map1)

map1


# In[23]:


#Adding some styling functions
style_function = "font-size: 12px; font-weight: bold"
choropleth.geojson.add_child(
    flm.features.GeoJsonTooltip(fields=['NAME_1','total_case','active_case','total_deaths',], aliases=['State', 'Total Case', 'Active', 'Deaths'], lables=True, sticky=True, toLocaleString=True, style=style_function))


# In[24]:


#Adding all the layers to map
flm.LayerControl().add_to(map1)


# In[25]:


#Finally rendering the map
map1.save('IndianMap.html')
map1


# In[ ]:




