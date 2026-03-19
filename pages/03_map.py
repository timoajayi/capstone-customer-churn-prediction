import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import functions as f

## Navigation
f.navigation()

## Page content
st.title("🌍 Customer Churn Analysis by Region")
st.subheader("Identifying high-risk geographic segments")

st.write(
    "This map visualizes customer churn patterns across different countries, "
    "highlighting regions where targeted retention strategies can have the greatest impact."
)

# Data prep
df_geo = st.session_state.df.copy()

geo_summary = df_geo.groupby("Geography").agg(
    churn_rate=("Exited", "mean"),
    total_customers=("Exited", "count"),
    avg_balance=("Balance", "mean")
).reset_index()

# Advanced map
fig = px.choropleth(
    geo_summary,
    locations="Geography",
    locationmode="country names",
    color="churn_rate",
    color_continuous_scale="Reds",
    hover_name="Geography",
    hover_data={
        "churn_rate": ":.2%",
        "total_customers": True,
        "avg_balance": ":,.0f"
    },
    projection="natural earth",
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="black",
    plot_bgcolor="black",
    geo=dict(
        bgcolor="black",
        showcoastlines=True,
        coastlinecolor="gray",
        landcolor="#1f1f1f",
        showocean=True,
        oceancolor="#0a0a0a"
    ),
    coloraxis_colorbar_title="Churn Rate"
)

st.plotly_chart(fig, use_container_width=True)

# Insight
highest = geo_summary.sort_values("churn_rate", ascending=False).iloc[0]

st.info(
    f"📍 {highest['Geography']} has the highest churn rate ({highest['churn_rate']:.2%}), "
    "indicating a need for targeted retention strategies."
)

