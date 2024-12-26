import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn

model=pickle.load(open('LinearRegressionModel.pkl','rb'))

car=pd.read_csv('Cleaned_cars.csv')
companies=sorted(car['company'].unique())
car_models=sorted(car['name'].unique())
year=sorted(car['year'].unique(),reverse=True)
fuel_type=car['fuel_type'].unique()

st.title("Car Price Predictor")

car_company = st.selectbox("Which company does your car belong to?", companies)
car_model = st.selectbox("Which car model is it?", car[car['company']==car_company]['name'].unique())
car_year = st.selectbox("Which year was the car bought?", year)
car_fuel_type = st.selectbox("Fuel type?", fuel_type)
kms_driven = st.number_input('kms_driven')

if st.button('Predict'):
    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'], 
                                          data=np.array([car_model,car_company,car_year,kms_driven,car_fuel_type]).reshape(1, 5)))
    st.text("The car may be sold for approximately Rs. "+str(int(prediction[0])))