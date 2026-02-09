import streamlit as st
import pandas as pd

# Title of the app
st.title("🍕 Pizza Project Data Analysis")

# 1. LOAD THE FILE

try:
    df = pd.read_csv('R6036699.csv')
    st.success("File loaded successfully!")

    # 2. BASIC DATA ANALYSIS
    
    # Show Shape
    st.subheader("1. Data Shape")
    st.write(f"The dataset has **{df.shape[0]}** rows and **{df.shape[1]}** columns.")

    # Show Column Names
    st.subheader("2. Column Names")
    st.write(list(df.columns))

    # Show Missing Values
    st.subheader("3. Missing Values")
    missing_data = df.isnull().sum()
    st.write(missing_data[missing_data > 0] if missing_data.sum() > 0 else "No missing values found!")

    # Show Data Preview
    st.subheader("4. Data Preview (First 5 rows)")
    st.dataframe(df.head())

    # Basic Statistics
    st.subheader("5. Basic Statistics")
    st.write(df.describe())

except FileNotFoundError:
    st.error(f"Error: The file was not found. Please check the path.")