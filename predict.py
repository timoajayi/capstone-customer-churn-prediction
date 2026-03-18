import streamlit as st
import sys
import pandas as pd
import pickle
import os
import warnings
warnings.filterwarnings('ignore')

# We load the model once and cache it to make the app faster and more efficient


@st.cache_resource
def load_all():
    filepath = os.path.join("models", "best_model.pkl")
    with open(filepath, "rb") as f:
        model = pickle.load(f)

    with open('label_encoder_gender.pkl', 'rb') as f:
        label_encoder_gender = pickle.load(f)

    with open('encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)

    return model, label_encoder_gender, encoder

model, label_encoder_gender, encoder = load_all()



## Define the streamlit app
st.title("Customer Churn Prediction")

# Create input fields for user to enter customer data
geography = st.selectbox("Geography", encoder.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input("Credit Score")
estimated_salary = st.number_input("Estimated Salary")
tenure = st.slider("Tenure", 0, 10)
num_of_products = st.slider("Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

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

if st.button("Predict Churn"):

    # 1. Encode Geography
    geo_encoded = encoder.transform(input_data[['Geography']]).toarray()

    geo_df = pd.DataFrame(
        geo_encoded,
        columns=encoder.get_feature_names_out(['Geography'])
    )

    # 2. Drop original Geography
    input_data_model = input_data.drop('Geography', axis=1)

    # 3. Combine
    input_data_model = pd.concat(
        [input_data_model.reset_index(drop=True), geo_df],
        axis=1
    )

    # 4. Align columns (VERY IMPORTANT)
    input_data_model = input_data_model.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    # 5. Predict probability
    prediction_probability = model.predict_proba(input_data_model)[0][1]

    # 6. Display result
    if prediction_probability > 0.5:
        st.error(f"⚠️ High Risk: Customer likely to churn ({prediction_probability:.2f})")
    else:
        st.success(f"✅ Low Risk: Customer likely to stay ({prediction_probability:.2f})")

    st.progress(int(prediction_probability * 100))

