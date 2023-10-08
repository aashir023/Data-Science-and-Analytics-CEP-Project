import streamlit as st
import pickle
import numpy as np
import requests

# Define the Streamlit app
st.title('Total Fare Prediction App')

# Input fields for user to enter data
st.header('Enter Taxi Ride Details:')
trip_duration = st.number_input('Trip Duration (minutes)', min_value=0)
distance_traveled = st.number_input('Distance Traveled (miles)', min_value=0.0)
num_of_passengers = st.number_input('Number of Passengers', min_value=1)
fare = st.number_input('Base Fare', min_value=0.0)
tip = st.number_input('Tip Amount', min_value=0.0)
miscellaneous_fees = st.number_input('Miscellaneous Fees', min_value=0.0)
surge_applied = st.radio('Surge Applied', ['No', 'Yes'])

# Convert surge_applied to binary (0 or 1)
surge_binary = 1 if surge_applied == 'Yes' else 0

# Load your trained regression model from GitHub
model_url = 'model.pkl'
response = requests.get(model_url)
your_model = pickle.loads(response.content)

# Button to predict total fare
if st.button('Predict Total Fare'):
    # Create a NumPy array with the input data
    input_data = np.array([[trip_duration, distance_traveled, num_of_passengers, fare, tip, miscellaneous_fees, surge_binary]])
    
    # Use the model to make a prediction
    prediction = your_model.predict(input_data)
    
    # Display the prediction
    st.subheader('Predicted Total Fare:')
    st.write(f'${prediction[0]:.2f}')
