import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import functions as f

st.set_page_config(
    page_title="Map",
    page_icon="🔴")

f.navigation()

st.title("🌍 Pokémon Map Visualization")
st.subheader("Where can we find these Pokémon?")
st.write("This page shows the geographical distribution of Pokémon based on their latitude and longitude coordinates. You can explore the map to see where different types of Pokémon are commonly found, and how their hit points vary across locations.")

# Option 1: Streamlit (simple)
st.subheader("Simple map - Streamlit")
st.map(st.session_state.df)


st.write(" ")
st.write("")


### Option 2: Plotly (advanced)
st.subheader("Advanced map - Plotly")

fig = px.scatter_geo(
    st.session_state.df,
    lat="latitude",
    lon="longitude",
    color="type",
    hover_name="name",
    size="hit_points",
    projection="natural earth",   # There are many options: mercator, orthographic, ..
    title="Distribution of Pokémon by generation and type"
)

st.plotly_chart(fig)
