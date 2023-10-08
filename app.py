import streamlit as st
import pickle
import numpy as np

# Define the Streamlit app
st.title('Taxi Fare Estimation')

# Introduction and explanation
st.markdown("This app estimates the total fare for a taxi ride based on various factors.")
st.markdown("Please enter the details of your ride on the left and click 'Predict Total Fare' to get an estimate.")

# Create a sidebar for user input
st.sidebar.header('Enter Taxi Ride Details:')
trip_duration = st.sidebar.number_input('Trip Duration (minutes)', min_value=0)
distance_traveled = st.sidebar.number_input('Distance Traveled (miles)', min_value=0.0)
num_of_passengers = st.sidebar.number_input('Number of Passengers', min_value=1)
fare = st.sidebar.number_input('Base Fare', min_value=0.0)
tip = st.sidebar.number_input('Tip Amount', min_value=0.0)
miscellaneous_fees = st.sidebar.number_input('Miscellaneous Fees', min_value=0.0)
surge_applied = st.sidebar.radio('Surge Applied', ['No', 'Yes'])

# Convert surge_applied to binary (0 or 1)
surge_binary = 1 if surge_applied == 'Yes' else 0

# Load your trained regression model from the specified path
model_path = r'C:\Users\Aashir\Desktop\Data-Science-and-Analytics-CEP-Project\model'  
with open(model_path, 'rb') as model_file:
    your_model = pickle.load(model_file)

# Add a button for prediction
if st.sidebar.button('Predict Total Fare'):
    # Create a NumPy array with the input data
    input_data = np.array([[trip_duration, distance_traveled, num_of_passengers, fare, tip, miscellaneous_fees, surge_binary]])
    
    # Use the model to make a prediction
    prediction = your_model.predict(input_data)
    
    # Display the prediction
    st.subheader('Predicted Total Fare:')
    st.write(f'${prediction[0]:.2f}')

# Additional styling and customization
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by [Aashir Ali]")
st.sidebar.markdown("[GitHub Repository](https://github.com/aashir023/Data-Science-and-Analytics-CEP-Project.git)")

# You can add more styling, explanations, or sections as needed
