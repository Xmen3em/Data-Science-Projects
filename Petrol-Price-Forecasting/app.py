import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
# Load the trained model
model = load_model('D:\Beginner-Projects\Petrol-Price-Forecasting\models\petrol_price_model.h5')

# Function to preprocess data (based on notebook pipeline)
def preprocess_data(data):
    data.rename(columns={"Petrol (USD)": "Petrol"}, inplace = True)
    data = data[data.Petrol < 160]  # Reintroduced filtering step
    # Example preprocessing steps (adjust based on your notebook)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data[['Petrol']])
    return data_scaled, scaler

# Function to analyze training data
def analyze_training_data(training_data):
    st.subheader("Training Data Analysis")
    training_data.rename(columns={"Petrol (USD)": "Petrol"}, inplace = True)
    training_data = training_data[training_data.Petrol < 160]  # Reintroduced filtering step
    # Display basic statistics
    st.write(training_data.describe())
    # Plotting time series
    plt.figure(figsize=(10, 5))
    plt.plot(training_data['Date'], training_data['Petrol'], label='Value over Time')
    plt.title('Training Data Time Series')
    plt.xlabel('Date')
    plt.ylabel('Petrol Price')
    plt.legend()
    st.pyplot(plt)

    # Correlation heatmap
    plt.figure(figsize=(10, 5))
    sns.heatmap(training_data.corr(), annot=True, cmap='coolwarm')
    st.title("Correlation Heatmap")
    st.pyplot(plt)

# Function to make predictions
def make_predictions(test_data, scaler):
    filtered_test_data = test_data[test_data.Petrol < 160]  # Apply filtering
    # Scale filtered test data
    test_data_scaled = scaler.transform(filtered_test_data[['Petrol']])
    predictions_scaled = model.predict(test_data_scaled)
    # Inverse transform predictions to original scale
    predictions = scaler.inverse_transform(predictions_scaled)
    # Return predictions along with the filtered test data
    return predictions, filtered_test_data

# Streamlit app layout
st.title("Time Series Analysis and Prediction Application")

# Upload training data
uploaded_training_file = st.file_uploader("Upload Training Data (CSV)", type=["csv"])
if uploaded_training_file is not None:
    training_data = pd.read_csv(uploaded_training_file)
    training_data['Date'] = pd.to_datetime(training_data['Date'])
    analyze_training_data(training_data)

# Upload test data for predictions
uploaded_test_file = st.file_uploader("Upload Test Data (CSV)", type=["csv"])
if uploaded_test_file is not None:
    test_data = pd.read_csv(uploaded_test_file)
    test_data['Date'] = pd.to_datetime(test_data['Date'])
    
    # Preprocess test data
    test_data_scaled, scaler = preprocess_data(test_data)
    
    # Make predictions
    predictions, filtered_test_data = make_predictions(test_data, scaler)
    filtered_test_data['Predictions'] = predictions  # Assign predictions to filtered data

    st.subheader("Predictions")
    st.write(filtered_test_data[['Petrol', 'Predictions']])

    # Visualize predictions
    plt.figure(figsize=(10, 5))
    plt.plot(filtered_test_data.index, filtered_test_data['Petrol'], label='Actual Values', color='blue')
    plt.plot(filtered_test_data.index, filtered_test_data['Predictions'], label='Predicted Values', color='orange')
    plt.title('Predictions on Test Data')
    plt.xlabel('Date')
    plt.ylabel('Petrol Price')
    plt.legend()
    st.pyplot(plt)