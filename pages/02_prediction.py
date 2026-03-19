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
geography = st.selectbox("Geography", encoder.categories_[0], key="geo")
gender = st.selectbox("Gender", label_encoder_gender.classes_, key="gender")
age = st.slider("Age", 18, 92, key="age")
balance = st.number_input('Balance', key="balance")
credit_score = st.number_input("Credit Score", key="credit")
estimated_salary = st.number_input("Estimated Salary", key="salary")
tenure = st.slider("Tenure", 0, 10, key="tenure")
num_of_products = st.slider("Number of Products", 1, 4, key="products")
has_cr_card = st.selectbox("Has Credit Card", [0, 1], key="card")
is_active_member = st.selectbox("Is Active Member", [0, 1], key="active")

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


THRESHOLD = 0.35

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







# st.title("⚡️ Is my Pokémon legendary??")
# st.subheader("Let's find out!")
# st.space("medium")
# st.subheader("Enter Pokémon Stats")

# col1, col2, col3 = st.columns(3)


# with col1:
#     attack = st.number_input('Attack', min_value=1, max_value=255, value=80, step=5)
#     sp_attack = st.number_input("Special Attack", min_value=1, max_value=255, value=75, step=5)

# with col2:
#     defense = st.slider('Defense', min_value=1, max_value=255, value=80)
#     sp_defense = st.slider("Special Defense", min_value=20, max_value=255, value=75)

# with col3:
#     hp_str = st.text_input('Hit points', '70')
#     try:
#         hit_points = int(hp_str)
#         if hit_points > 255:
#             st.warning("HP cannot exceed 255. Setting to 255.")
#             hit_points = 255
#         elif hit_points < 1:
#             st.warning("HP must be at least 1. Setting to 1.")
#             hit_points = 1
#     except ValueError:
#         st.warning("Please enter a valid integer for HP.")
#         hit_points = 70
    
#     speed_str = st.text_input("Speed", "10")
#     try:
#         speed = int(speed_str)
#         if speed > 255:
#             st.warning("Speed cannot exceed 255. Setting to 255.")
#             speed = 255
#         elif speed < 5:
#             st.warning("Speed must be at least 5. Setting to 5.")
#             speed = 5
#     except ValueError:
#         st.warning("Please enter a valid integer for the speed.")
#         speed = 10

# if st.button('Predict!'):
#     features = {
#         "hit_points": hit_points,
#         "attack": attack,
#         "defense": defense,
#         "sp_attack": sp_attack,
#         "sp_defense": sp_defense,
#         "speed": speed
#     }

#     y_pred, y_prob = predict(features)

#     if y_pred == 1:
#         st.success(f'✅ This Pokemon is **Legendary!** (probability = {y_prob:.2%})')
#         st.balloons()
#     else:
#         st.info(f'❌ This Pokemon is **not Legendary!** (probability of the pokemon being legendary = {y_prob:.2%})')
#         st.snow()