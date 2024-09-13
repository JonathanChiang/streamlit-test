import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = pd.DataFrame({
    'name': ['Cafe A', 'Cafe B', 'Cafe C'],
    'lat': [37.7749, 37.7849, 37.7649],
    'lon': [-122.4194, -122.4294, -122.4094],
    'rating': [4.5, 4.0, 3.8],
    'review_count': [120, 95, 80],
    'address': ['123 Market St', '456 Mission St', '789 Castro St']
})

# Title
st.title("Basic Streamlit App with Plotly Map")

# Plotly Map
fig = px.scatter_mapbox(
    data,
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data={"rating": True, "review_count": True, "address": True},
    zoom=12,
    mapbox_style="open-street-map"
)

# Display the map in Streamlit
st.plotly_chart(fig)

# Display the table
st.write("List of Cafes:")
st.dataframe(data[['name', 'rating', 'review_count', 'address']])
