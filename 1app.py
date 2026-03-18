import streamlit as st
import pandas as pd
import numpy as np
from functions import navigation
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='Pokemon', 
                   page_icon=':smiley:', 
                   layout='wide'
                   )

navigation()
# Write title/header
st.title("Welcome to my Pokemon")

#st.markdown('Hi!!')
st.image('images/pic.png')
st.subheader('What is your favourite Pokemon?')
st.markdown('- EDA Visualizations / Dataset exploration \n - __Prediction:__ Is my Pokemon legendary? \n - Find our Pokemon in the map')

# Save variabale to session state
# Save variables in the session state
st.session_state.df = pd.read_csv('data/Churn_Modelling.csv')