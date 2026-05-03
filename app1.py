import pickle 
import pandas as pd
import numpy as np
import streamlit as st
df=pickle.load(open(r'C:/Users/dell/DataScienceDeploymentProject/diabetes_prediction.sav','rb'))
st.title("Welcome to Diabetes prediction Website")
st.info("This web site help you to discover diabetes🧐")
st.sidebar.header("feature selection")

Pregnancies=st.text_input("Pregnancies")
Glucose=st.text_input("Glucose")
BloodPressure=st.text_input("BloodPressure")
SkinThickness=st.text_input("SkinThickness")
Insulin=st.text_input("Insulin")
BMI=st.text_input("BMI")
DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
Age=st.text_input("Age")

data=pd.DataFrame({'Pregnancies':[Pregnancies], 'Glucose':[Glucose], 'BloodPressure':[BloodPressure], 'SkinThickness':SkinThickness, 'Insulin':Insulin,
       'BMI':[BMI], 'DiabetesPedigreeFunction':[DiabetesPedigreeFunction], 'Age':[Age]},index=[0])
con=st.sidebar.button("predict")
if con:
    result=df.predict(data)
    if result==0:
        st.write("No, there is not diabetes disease")
    else:
        st.write("Yes, there is  diabetes disease")
