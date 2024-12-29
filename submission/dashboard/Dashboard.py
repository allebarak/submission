import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk visualisasi pola penggunaan sepeda secara musiman atau bulanan
def visualisasi_bulanan(data_day_cleaned):
    # Agregasi rata-rata pengguna sepeda per bulan
    monthly_usage = data_day_cleaned.groupby('mnth')['cnt'].mean().reset_index()

    # Map angka bulan ke nama bulan untuk keterbacaan
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_usage['mnth'] = monthly_usage['mnth'].map(lambda x: month_names[x - 1])

    # Visualisasi rata-rata penggunaan sepeda per bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(x='mnth', y='cnt', data=monthly_usage, palette='Blues_d')
    plt.title('Rata-Rata Penggunaan Sepeda per Bulan', fontsize=16)
    plt.xlabel('Bulan', fontsize=14)
    plt.ylabel('Rata-Rata Pengguna', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Fungsi untuk visualisasi pengaruh cuaca terhadap jumlah pengguna sepeda
def visualisasi_cuaca(data_day_cleaned):
    # Agregasi rata-rata pengguna sepeda berdasarkan kondisi cuaca
    weather_usage = data_day_cleaned.groupby('weathersit')['cnt'].mean().reset_index()

    # Map kondisi cuaca ke deskripsi yang lebih jelas
    weather_labels = {1: 'Cerah/Berawan', 2: 'Berkabut/Berawan', 3: 'Hujan Salju Ringan', 4: 'Hujan Salju Deras'}
    weather_usage['weathersit'] = weather_usage['weathersit'].map(weather_labels)

    # Visualisasi rata-rata penggunaan sepeda berdasarkan kondisi cuaca
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_usage, palette='coolwarm')
    plt.title('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda', fontsize=16)
    plt.xlabel('Kondisi Cuaca', fontsize=14)
    plt.ylabel('Rata-Rata Pengguna', fontsize=14)
    plt.xticks(rotation=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

