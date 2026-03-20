from pyexpat import model

import streamlit as st
import functions as f
#from utils.predict import load_all, predict_churn
import pandas as pd
import os
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

f.navigation()


@st.cache_resource
def load_all():
    # Load artifact
    filepath = os.path.join("models", "churn_model.pkl")
    with open(filepath, "rb") as f:
        artifact = pickle.load(f)

    model = artifact["model"]
    threshold = artifact["threshold"]

    # Load encoders
    with open(os.path.join("models", "label_encoder_gender.pkl"), 'rb') as f:
        label_encoder_gender = pickle.load(f)

    with open(os.path.join("models", "encoder.pkl"), 'rb') as f:
        encoder = pickle.load(f)

    return model, threshold, label_encoder_gender, encoder

model, threshold, label_encoder_gender, encoder = load_all()

## Define the streamlit app
st.title("Customer Churn Prediction")

# Create input fields for user to enter customer data
credit_score = st.number_input("Credit Score", key="credit")
geography = st.selectbox("Geography", encoder.categories_[0], key="geo")
gender = st.selectbox("Gender", label_encoder_gender.classes_, key="gender")
age = st.slider("Age", 18, 92, key="age")
tenure = st.slider("Tenure", 0, 10, key="tenure")
balance = st.number_input('Balance', key="balance")
num_of_products = st.slider("Number of Products", 1, 4, key="products")
has_cr_card = st.selectbox("Has Credit Card", [0, 1], key="card")
is_active_member = st.selectbox("Is Active Member", [0, 1], key="active")
estimated_salary = st.number_input("Estimated Salary", key="salary")

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
    'Geography': [geography]
})


def predict_churn(input_data, model, label_encoder_gender, encoder):
    
    # Encode Geography
    geo_encoded = encoder.transform(input_data[['Geography']]).toarray()

    geo_df = pd.DataFrame(
        geo_encoded,
        columns=encoder.get_feature_names_out(['Geography'])
    )

    # Drop original Geography
    input_data_model = input_data.drop('Geography', axis=1)

    # Combine
    input_data_model = pd.concat(
        [input_data_model.reset_index(drop=True), geo_df],
        axis=1
    )

    # Align columns
    input_data_model = input_data_model.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    # Predict
    prediction_probability = model.predict_proba(input_data_model)[0][1]

    return prediction_probability


THRESHOLD = 0.31

if st.button("Predict Churn", key="predict_btn"):

    prediction_probability = predict_churn(
        input_data,
        model,
        label_encoder_gender,
        encoder
    )

    # Display result
    if prediction_probability > THRESHOLD:
        st.error(f"⚠️ High Risk: Customer likely to churn ({prediction_probability:.2%})")
    else:
        st.success(f"✅ Low Risk: Customer likely to stay ({prediction_probability:.2%})")

    # Progress bar
    st.progress(int(prediction_probability * 100))

    # Explanation
    st.caption(f"Threshold set at {THRESHOLD} to improve recall and detect more at-risk customers.")



# @st.cache_resource
# def load_all():
#     filepath = os.path.join("models", "churn_model.pkl")
#     with open(filepath, "rb") as f:
#         artifact = pickle.load(f)

#     model = artifact["model"]
#     threshold = artifact["threshold"]

#     with open('label_encoder_gender.pkl', 'rb') as f:
#         label_encoder_gender = pickle.load(f)

#     with open('encoder.pkl', 'rb') as f:
#         encoder = pickle.load(f)

#     return model, label_encoder_gender, encoder

# model, label_encoder_gender, encoder = load_all()

