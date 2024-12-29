import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache
def load_data():
    day_data_path = 'day.csv'  # Update this path if necessary
    data_day_cleaned = pd.read_csv(day_data_path)
    return data_day_cleaned

data_day_cleaned = load_data()

# Streamlit app title
st.title('Bike Sharing Dashboard')

st.sidebar.title('Navigation')
options = st.sidebar.radio('Select an option:', ['Monthly Analysis', 'Weather Analysis'])

# Function for Monthly Analysis
def visualisasi_bulanan(data):
    monthly_usage = data.groupby('mnth')['cnt'].mean().reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_usage['mnth'] = monthly_usage['mnth'].map(lambda x: month_names[x - 1])

    plt.figure(figsize=(12, 6))
    sns.barplot(x='mnth', y='cnt', data=monthly_usage, palette='Blues_d')
    plt.title('Rata-Rata Penggunaan Sepeda per Bulan', fontsize=16)
    plt.xlabel('Bulan', fontsize=14)
    plt.ylabel('Rata-Rata Pengguna', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Function for Weather Analysis
def visualisasi_cuaca(data):
    weather_usage = data.groupby('weathersit')['cnt'].mean().reset_index()
    weather_labels = {1: 'Cerah/Berawan', 2: 'Berkabut/Berawan', 3: 'Hujan Salju Ringan', 4: 'Hujan Salju Deras'}
    weather_usage['weathersit'] = weather_usage['weathersit'].map(weather_labels)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_usage, palette='coolwarm')
    plt.title('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda', fontsize=16)
    plt.xlabel('Kondisi Cuaca', fontsize=14)
    plt.ylabel('Rata-Rata Pengguna', fontsize=14)
    plt.xticks(rotation=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Monthly Analysis Section
if options == 'Monthly Analysis':
    st.header('Monthly Analysis')
    visualisasi_bulanan(data_day_cleaned)

# Weather Analysis Section
elif options == 'Weather Analysis':
    st.header('Weather Analysis')
    visualisasi_cuaca(data_day_cleaned)
