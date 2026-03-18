import streamlit as st
import functions as f
from predict import prediction_probability 

st.set_page_config(
    page_title="Is it legendary?",
    page_icon="🔴")

f.navigation()

st.title("⚡️ Is my Pokémon legendary??")
st.subheader("Let's find out!")
st.space("medium")
st.subheader("Enter Pokémon Stats")

col1, col2, col3 = st.columns(3)


with col1:
    attack = st.number_input('Attack', min_value=1, max_value=255, value=80, step=5)
    sp_attack = st.number_input("Special Attack", min_value=1, max_value=255, value=75, step=5)

with col2:
    defense = st.slider('Defense', min_value=1, max_value=255, value=80)
    sp_defense = st.slider("Special Defense", min_value=20, max_value=255, value=75)

with col3:
    hp_str = st.text_input('Hit points', '70')
    try:
        hit_points = int(hp_str)
        if hit_points > 255:
            st.warning("HP cannot exceed 255. Setting to 255.")
            hit_points = 255
        elif hit_points < 1:
            st.warning("HP must be at least 1. Setting to 1.")
            hit_points = 1
    except ValueError:
        st.warning("Please enter a valid integer for HP.")
        hit_points = 70
    
    speed_str = st.text_input("Speed", "10")
    try:
        speed = int(speed_str)
        if speed > 255:
            st.warning("Speed cannot exceed 255. Setting to 255.")
            speed = 255
        elif speed < 5:
            st.warning("Speed must be at least 5. Setting to 5.")
            speed = 5
    except ValueError:
        st.warning("Please enter a valid integer for the speed.")
        speed = 10

if st.button('Predict!'):
    features = {
        "hit_points": hit_points,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed
    }

    y_pred, y_prob = predict(features)

    if y_pred == 1:
        st.success(f'✅ This Pokemon is **Legendary!** (probability = {y_prob:.2%})')
        st.balloons()
    else:
        st.info(f'❌ This Pokemon is **not Legendary!** (probability of the pokemon being legendary = {y_prob:.2%})')
        st.snow()