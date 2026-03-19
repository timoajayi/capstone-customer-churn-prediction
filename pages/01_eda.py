import streamlit as st
import pandas as pd 
from functions import navigation
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import streamlit as st   

navigation()
st.session_state.df = pd.read_csv('data/Churn_Modelling.csv')

df1 = st.session_state.df.copy()

## Page content
st.title("Exploratory Data Analysis")

st.markdown("### 📊 Customer Churn Distribution")

## Target variable distribution
counts = df1["Exited"].value_counts().sort_index()

df_plot = counts.reset_index()
df_plot.columns = ["Exited", "Count"]

df_plot["Label"] = df_plot["Exited"].map({0: "Stayed", 1: "Churned"})

fig = px.bar(
    df_plot,
    x="Label",
    y="Count",
    color="Label",
    text="Count",
    color_discrete_map={
        "Stayed": "steelblue",
        "Churned": "salmon"
    }
)

fig.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Number of Customers",
    showlegend=False,   # cleaner since labels already shown
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "The dataset is imbalanced, with significantly more customers staying than churning. "
    "This means accuracy alone is not sufficient, and metrics like recall and F1-score are more important."
)

#2) second plot - churn by tenure
st.subheader("⏳ Churn by Customer Tenure")

df1['Tenure_group'] = pd.cut(
    df1['Tenure'],
    bins=[0,2,5,8,10],
    labels=['0-2','3-5','6-8','9-10']
)

# Better labels
df1["Churn_Label"] = df1["Exited"].map({0: "Stayed", 1: "Churned"})

fig = px.histogram(
    df1,
    x='Tenure_group',
    color='Churn_Label',
    barmode='group',
    text_auto=True,
    color_discrete_map={
        "Stayed": "steelblue",
        "Churned": "salmon"
    }
)

fig.update_layout(
    xaxis_title='Tenure Group (Years)',
    yaxis_title='Number of Customers',
    template="plotly_dark"  # matches your map
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "Customers with fewer years at the bank show higher churn rates, indicating that retention efforts should focus on early customer engagement. "
    "Improving onboarding experience and initial product adoption could significantly reduce churn."
)
