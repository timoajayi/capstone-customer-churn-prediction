## import the necessary packages
import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
import pickle
from functions import navigation
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title='Customer Churn Dashboard',
    page_icon='📊',
    layout='wide'
)

navigation()
# Write title/header
st.title("🚀 Customer Churn Intelligence Dashboard")

#st.markdown('Hi!!')
st.image('images/pic.png')
st.markdown("""
This application helps banks understand and predict customer churn using data and machine learning.

### 🔍 Explore:
- 📊 Customer behavior and churn patterns  
- 🤖 Predict churn risk  
- 🌍 Identify high-risk regions  

💡 Built to support data-driven retention strategies and improve customer lifetime value.
""")

st.markdown("---")

st.subheader("📌 How to use this dashboard")

st.markdown("""
1. Go to **EDA** → explore patterns in the data  
2. Use **Prediction** → test churn risk  
3. View **Geography** → identify high-risk regions  
""")

# Save variabale to session state
# Save variables in the session state
st.session_state.df = pd.read_csv('data/Churn_Modelling.csv')








# # Load the trained model and encoders
# @st.cache_resource
# def load_model():
#     return tf.keras.models.load_model('churn_model.h5')

# ann_model = load_model()

# # Load the encoders
# with open('label_encoder_gender.pkl', 'rb') as f:
#     label_encoder_gender = pickle.load(f)

# with open('encoder.pkl', 'rb') as f:
#     encoder = pickle.load(f)

# with open('scaler.pkl', 'rb') as f:
#     scaler = pickle.load(f)


# ## Define the streamlit app
# st.title("Customer Churn Prediction")

# # Create input fields for user to enter customer data
# geography = st.selectbox("Geography", encoder.categories_[0])
# gender = st.selectbox("Gender", label_encoder_gender.classes_)
# age = st.slider("Age", 18, 92)
# balance = st.number_input('Balance')
# credit_score = st.number_input("Credit Score")
# estimated_salary = st.number_input("Estimated Salary")
# tenure = st.slider("Tenure", 0, 10)
# num_of_products = st.slider("Number of Products", 1, 4)
# has_cr_card = st.selectbox("Has Credit Card", [0, 1])
# is_active_member = st.selectbox("Is Active Member", [0, 1])

# input_data = pd.DataFrame({
#     'CreditScore': [credit_score],
#     'Gender': [label_encoder_gender.transform([gender])[0]],
#     'Age': [age],
#     'Tenure': [tenure],
#     'Balance': [balance],
#     'NumOfProducts': [num_of_products],
#     'HasCrCard': [has_cr_card],
#     'IsActiveMember': [is_active_member],
#     'EstimatedSalary': [estimated_salary],
#     'Geography': [geography]
# })
 


# ## One-hot encode Geography
# geo_encoded = encoder.transform(input_data[['Geography']]).toarray()

# geo_df = pd.DataFrame(
#     geo_encoded,
#     columns=encoder.get_feature_names_out(['Geography'])
# )

# ## Drop original Geography
# input_data = input_data.drop('Geography', axis=1)

# ## Combine the one-hot encoded Geography with the rest of the input data
# input_data = pd.concat([input_data.reset_index(drop=True), geo_df], axis=1)

# ## Align columns with training data
# input_data = input_data.reindex(columns=scaler.feature_names_in_, fill_value=0)

# ## Scale the input data
# input_data_scaled = scaler.transform(input_data)

# ### Make predictions using the loaded model
# if st.button("Predict Churn"):
#     prediction = ann_model.predict(input_data_scaled, verbose=0)
#     prediction_probability = prediction[0][0]

#     if prediction_probability > 0.5:
#         st.write(f"The customer is likely to churn with a probability of {prediction_probability:.2f}.")
#     else:
#         st.write(f"The customer is unlikely to churn with a probability of {prediction_probability:.2f}.")