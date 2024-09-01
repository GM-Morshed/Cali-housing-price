import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('Model/random_forest_model.pkl')

# Streamlit app layout
st.title('Housing Price Application')
st.header('This is a heading item')

