# Diabetes_Predictor

A simple Streamlit web app that predicts the likelihood of diabetes based on health metrics using a pre-trained machine learning model.

# Features

a.) Enter patient health data (glucose, insulin, BMI, age, etc.)

b.) Uses a trained machine learning model (diabetes_model.pkl) with scaled input (scaler.pkl).

c.) Displays an intuitive risk assessment:

✅ Not likely to have diabetes

⚠️ Likely to have diabetes

# How it works

Takes user input of:

Pregnancies,
Glucose,
Blood Pressure,
Skin Thickness,
Insulin,
BMI,
Diabetes Pedigree Function,
Age

Scales it using the loaded scaler.

Passes it to the trained classifier.

Outputs prediction.

# Install dependencies

pip install streamlit, numpy, scikit-learn, matplotlib, seaborn, pickle

# Running the app

streamlit run app.py
