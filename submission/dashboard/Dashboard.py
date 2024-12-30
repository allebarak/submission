import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Dynamically get the absolute path of the CSV files
current_dir = os.path.dirname(os.path.abspath(__file__))
hour_data_path = os.path.join(current_dir, 'hour.csv')
day_data_path = os.path.join(current_dir, 'day.csv')

# Load your dataset
@st.cache
def load_data():
    data_hour = pd.read_csv(hour_data_path)
    data_day = pd.read_csv(day_data_path)
    return data_hour, data_day

data_hour, data_day = load_data()

def clean_data(df):
    """
    Fungsi untuk membersihkan dataset:
    1. Menyesuaikan tipe data jika diperlukan
    """
    print(f"--- Sebelum Pembersihan ---")
    print(f"Tipe Data Tiap Kolom:\n{df.dtypes}")
    print("-" * 50)

    # Konversi tipe data jika diperlukan (contoh: kolom tanggal)
    if 'dteday' in df.columns:  # Jika kolom 'dteday' ada di dataset
        df['dteday'] = pd.to_datetime(df['dteday'], errors='coerce')

    print(f"--- Setelah Pembersihan ---")
    print(f"Tipe Data Tiap Kolom Setelah Penyesuaian:\n{df.dtypes}")
    print("-" * 50)

    return df

# Membersihkan Dataset Day
data_day_cleaned = clean_data(data_day)

# Membersihkan Dataset Hour
data_hour_cleaned = clean_data(data_hour)

# Streamlit app title
st.title('Bike Sharing Dashboard')

st.sidebar.title('Navigation')
options = st.sidebar.radio('Select an option:', ['Monthly Analysis', 'Weather Analysis', 'Seasonal Analysis'])

# Function for filtering data by date range
def filter_by_date(data):
    if 'dteday' in data.columns:
        start_date = st.sidebar.date_input('Start Date', data['dteday'].min().date())
        end_date = st.sidebar.date_input('End Date', data['dteday'].max().date())

        filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]
        return filtered_data
    return data

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

# Function for Seasonal Analysis
def visualisasi_musiman(data):
    seasonal_usage = data.groupby('season')['cnt'].mean().reset_index()
    season_names = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
    seasonal_usage['season'] = seasonal_usage['season'].map(season_names)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=seasonal_usage, palette='coolwarm')
    plt.title('Rata-Rata Penggunaan Sepeda per Musim', fontsize=16)
    plt.xlabel('Musim', fontsize=14)
    plt.ylabel('Rata-Rata Pengguna', fontsize=14)
    plt.xticks(rotation=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Monthly Analysis Section
if options == 'Monthly Analysis':
    st.header('Monthly Analysis')
    filtered_data = filter_by_date(data_day_cleaned)
    visualisasi_bulanan(filtered_data)

# Weather Analysis Section
elif options == 'Weather Analysis':
    st.header('Weather Analysis')
    filtered_data = filter_by_date(data_day_cleaned)
    visualisasi_cuaca(filtered_data)

# Seasonal Analysis Section
elif options == 'Seasonal Analysis':
    st.header('Seasonal Analysis')
    filtered_data = filter_by_date(data_day_cleaned)
    visualisasi_musiman(filtered_data)
