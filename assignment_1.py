import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (m):")

if weight and height:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
