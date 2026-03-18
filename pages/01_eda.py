import streamlit as st
import pandas as pd 
from functions import navigation
import plotly.express as px
import plotly.graph_objects as go   

navigation()
st.session_state.df = pd.read_csv('data/Churn_Modelling.csv')
# st.session_state.stats_cols = ['hit_points', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']


# fig = px.scatter(
#     st.session_state.df,
#     x='height_m',
#     y='weight_kg',
#     color='type',
#     size='speed',
#     title='Height vs Weight (Plotly)',
#     hover_data=['name']
# )


# fig.update_traces(
#     hovertemplate=
#     '<b>Name:</b> %{customdata[0]}<br>' +
#     '<b>Height (m):</b> %{x}<br>' +
#     '<b>Weight (kg):</b> %{y}<br>' +
#     '<b>Type:</b> %{customdata[1]}<br>' +
#     '<b>Speed:</b> %{customdata[2]}<br>' +
#     '<extra></extra>', 
#     customdata=st.session_state.df[['name', 'type', 'speed']].values)

# st.plotly_chart(fig)


# # Radar chart

# st.subheader('Pokémon Stats Radar Chart')

# pokemon_name = st.selectbox(
#     'Select Pokemon',
#     st.session_state.df['name'].tolist(),
#     key="pokemon"
# )

# pokemon_row = st.session_state.df[st.session_state.df['name']==pokemon_name].iloc[0]

# fig = go.Figure()

# fig.add_trace(go.Scatterpolar(
#               r=pokemon_row[st.session_state.stats_cols].values,
#               theta=st.session_state.stats_cols,
#               fill='toself',
#               name=pokemon_name)
# )

# st.plotly_chart(fig)
