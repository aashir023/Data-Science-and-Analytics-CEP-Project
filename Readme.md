# Taxi Fare Prediction Project

## Overview

This project aims to develop a machine learning model for predicting taxi fares based on various input features related to taxi rides. The model is designed to estimate the total fare of a taxi ride, taking into account factors such as trip duration, distance traveled, number of passengers, base fare, tips, miscellaneous fees, and surge pricing.

The project includes data collection, data preprocessing, model development, evaluation, and deployment on a Streamlit server. Below are the key details and findings of the project:

## Project Details

### Group Members
**Aashir Ali (20SW023)**

**Shehzad Haider (20SW067)**

**Ghansham Soomarani (20SW081)**

### Dataset
- **Source:** https://www.kaggle.com/datasets/raviiloveyou/predict-taxi-fare-with-a-bigquery-ml-forecasting
- **Description:** The dataset used in this project contains information about individual taxi rides, including features such as trip duration, distance traveled, number of passengers, fare, tip, miscellaneous fees, total fare, and surge pricing.

### Data Analysis
- Summary statistics for numerical features were calculated, providing insights into the central tendencies and dispersions of the data.
- Missing value counts for numerical features were examined to assess data completeness.
- A correlation matrix was computed to understand relationships between numerical features.
- The distribution of surge pricing (surge_applied) was analyzed to gain insights into its prevalence.

### Machine Learning
- A machine learning model, specifically a regression model, was developed to predict taxi fares based on the dataset.
- Model evaluation metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared score, were used to assess the model's performance.

### Deployment
- The trained model was deployed on a Streamlit server, allowing users to interact with the model through a user-friendly web interface.
- Users can input ride-related information, and the model will provide an estimated fare in real-time.

## Blog post
Link : https://medium.com/@aashirali619/predicting-taxi-fares-with-machine-learning-a-data-science-project-7005b381a173

Please read my blog post on Medium about this project where i have explained this project in detail.

## Dependencies
- Python (version X.X)
- Libraries: pandas, numpy, matplotlib scikit-learn, streamlit

## Contributors
- Aashir Ali
- Ghansham Soomarani
- Shahzad Haider

## Acknowledgments
- Kaggle : From where i downloaded this dataset

