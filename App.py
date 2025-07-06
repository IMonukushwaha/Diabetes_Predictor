import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Diabetes Predictor")
st.write("Enter patient info to check the risk of diabetes.")

# Input fields
preg = st.number_input('Pregnancies')
gluc = st.number_input('Glucose')
bp = st.number_input('Blood Pressure')
skin = st.number_input('Skin Thickness')
insulin = st.number_input('Insulin')
bmi = st.number_input('BMI')
dpf = st.number_input('Diabetes Pedigree Function')
age = st.number_input('Age')

if st.button('Predict'):
    input_data = np.array([[preg, gluc, bp, skin, insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ The person is likely to have diabetes.")
    else:
        st.success("✅ The person is not likely to have diabetes.")
