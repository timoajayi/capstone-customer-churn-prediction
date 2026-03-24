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

PRIMARY = "#1f77b4"   # blue
ALERT   = "#d62728"   # red

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
        "Stayed": PRIMARY,
        "Churned": ALERT
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
        "Stayed": PRIMARY,
        "Churned": ALERT
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
    "Improving onboarding experience and targeted incentives to build loyalty from the beginning."
)


st.subheader("📈 Model Performance Comparison")

results_df = pd.DataFrame({
    "Model": [
        #"Logistic Regression",
        "Gradient Boosting",
        "LGBMClassifier",
        "XGBoost"
    ],
    "Recall": [0.74, 0.61, 0.60], # logistic regression recall is 0.52, but I want to focus on the tree-based models since they are more interpretable and better for tabular data, so I will remove it from the plot.
    "F1 Score": [0.61, 0.62, 0.61] # logistic regression F1 score is 0.49, but I want to focus on the tree-based models since they are more interpretable and better for tabular data, so I will remove it from the plot.
})

results_melted = results_df.melt(
    id_vars="Model",
    value_vars=["Recall", "F1 Score"],
    var_name="Metric",
    value_name="Score"
)

fig = px.bar(
    results_melted,
    x="Model",
    y="Score",
    color="Metric",
    barmode="group",
    color_discrete_map={
        "Recall": PRIMARY,
        "F1 Score": ALERT
    }

)

st.plotly_chart(fig, use_container_width=True)
st.success("🏆 Gradient Boosting performs best, achieving the highest recall (74%), meaning it is most effective at identifying customers likely to churn.")