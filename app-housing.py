import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# set titile & read the file
st.title('California Housing Data (1990) by LiuNian')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Median House Price:',  0, 500001, 200000)  # min, max, default

# create a multi select 
location_filter = st.sidebar.multiselect(
     'Chose the location type',   # title
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults top 3 countries in population

# create a radio button selection
income_filter = st.sidebar.radio(
        'Choose income level',     # title
        ('Low', 'Median', 'High'))   # options

# filter by house value(median_house_value)
df = df[df.median_house_value <= price_filter]

# filter by location(ocean_proximity)
df = df[df.ocean_proximity.isin(location_filter)]

# filter by income
if income_filter == 'Low':
    df = df[df.median_income <= 2.5 ]
elif income_filter == 'High':
    df = df[df.median_income > 4.5 ]
else:
    df = df[(df.median_income < 4.5) & (df.median_income > 2.5) ]

# show on map
st.subheader('See More filters in the sidebar: ')
st.map(df)

# show the histogram
st.subheader('Histogram of The Miedian House Value')
fig , ax = plt.subplots(figsize=(20, 5))
df.median_house_value.hist(bins = 30)
st.pyplot(fig)



