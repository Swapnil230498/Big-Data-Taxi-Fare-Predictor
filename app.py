import pickle
import streamlit as st
import numpy as np
import vaex


#Importing model:
model = pickle.load(open("model_SGD.pkl",'rb'))

st.title('Taxi Trip Fare Calculator')

#asking user for Vendor ID:
vendor_id = st.selectbox("Vendor ID",['Creative Mobile Technologies','VeriFone Inc.'])

#asking user for no of passengers:
passenger_count = st.selectbox("No of Passengers travelling",[1,2,3,4,5,6])

#asking user for trip distance:
trip_distance = st.number_input('Distance travelled for this trip')

#asking user for rate code ID:
rate_code_id = st.selectbox('Rate code ID',['Standard rate','JFK','Newark','Nassau or Westchester','Negotiated fare','Group ride'])

if st.button('Predict Fare'):
    if vendor_id == 'Creative Mobile Technologies':
        vendorid=1
    else:
        vendorid=2
    
    if rate_code_id == 'Standard rate':
        ratecodeid = 1
    if rate_code_id == 'JFK':
        ratecodeid = 2
    if rate_code_id == 'Newark':
        ratecodeid = 3
    if rate_code_id == 'Nassau or Westchester':
        ratecodeid = 4
    if rate_code_id == 'Negotiated fare':
        ratecodeid = 5
    if rate_code_id == 'Group ride':
        ratecodeid = 6


   # Prepare the input features as a Vaex DataFrame
    query = vaex.from_arrays(vendorid=[vendorid], passenger_count=[passenger_count], trip_distance=[trip_distance], ratecodeid=[ratecodeid])

    # Make predictions using the trained model
    predicted_fare = model.transform(query).evaluate('prediction')

    st.title('Predicted Fare for your ride: ' + str(int(predicted_fare[0])))
