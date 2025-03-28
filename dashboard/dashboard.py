import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = 'data/data.csv'
data = pd.read_csv(file_path)

data_clean = data.drop_duplicates()
data_clean['datetime'] = pd.to_datetime(data_clean[['year', 'month', 'day', 'hour']])

bins = [0, 50, 100, 150, np.inf]
labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
data_clean['PM2.5_Kategori'] = pd.cut(data_clean['PM2.5'], bins=bins, labels=labels)

st.title('Dashboard Kualitas Udara dan Cuaca Aotizhongxin')

analysis_option = st.sidebar.selectbox('Pilih Analisis', ['Distribusi Polusi Udara', 'Tren PM2.5 Seiring Waktu', 'Korelasi Cuaca dan PM2.5', 'Distribusi PM2.5 Berdasarkan Kategori'])

st.sidebar.write("### Deskripsi Dashboard")
st.sidebar.write("""
Pada dashboard ini, kita akan melakukan analisis terhadap data kualitas udara dan cuaca yang diambil dari stasiun Aotizhongxin.
Berikut adalah beberapa analisis yang bisa dipilih:
1. **Distribusi Polusi Udara**: Menganalisis distribusi PM2.5 dan PM10 untuk melihat bagaimana polusi udara tersebar dalam dataset.
2. **Tren PM2.5 Seiring Waktu**: Melihat apakah ada tren perubahan dalam kualitas udara seiring waktu.
3. **Korelasi Cuaca dan PM2.5**: Menganalisis hubungan antara faktor cuaca (suhu, curah hujan, kecepatan angin) dan kualitas udara.
4. **Distribusi PM2.5 Berdasarkan Kategori**: Melihat distribusi PM2.5 berdasarkan kategori rendah, sedang, tinggi, dan sangat tinggi.
""")

# Analisis 1: Distribusi Polusi Udara
if analysis_option == 'Distribusi Polusi Udara':
    st.subheader('Distribusi PM2.5 dan PM10')
    st.write("Pada analisis ini, kita akan melihat distribusi polusi udara berdasarkan PM2.5 dan PM10.")
    col1, col2 = st.columns(2)

    # Distribusi PM2.5
    with col1:
        st.write("Distribusi PM2.5")
        fig, ax = plt.subplots()
        sns.histplot(data_clean['PM2.5'], kde=True, color='skyblue', ax=ax)
        st.pyplot(fig)

    # Distribusi PM10
    with col2:
        st.write("Distribusi PM10")
        fig, ax = plt.subplots()
        sns.histplot(data_clean['PM10'], kde=True, color='salmon', ax=ax)
        st.pyplot(fig)

# Analisis 2: Tren PM2.5 Seiring Waktu
elif analysis_option == 'Tren PM2.5 Seiring Waktu':
    st.subheader('Tren Rata-rata PM2.5 Seiring Waktu')
    st.write("Pada analisis ini, kita akan melihat tren perubahan konsentrasi PM2.5 seiring waktu.")
    fig, ax = plt.subplots(figsize=(12, 6))
    data_clean.groupby('datetime')['PM2.5'].mean().plot(ax=ax)
    ax.set_title('Rata-rata Konsentrasi PM2.5 Seiring Waktu', fontsize=14)
    ax.set_xlabel('Waktu', fontsize=12)
    ax.set_ylabel('Rata-rata PM2.5', fontsize=12)
    ax.grid(True)
    st.pyplot(fig)

# Analisis 3: Korelasi Cuaca dan PM2.5
elif analysis_option == 'Korelasi Cuaca dan PM2.5':
    st.subheader('Korelasi PM2.5 dengan Faktor Cuaca')
    st.write("Pada analisis ini, kita akan menganalisis hubungan antara PM2.5 dan beberapa faktor cuaca.")
    weather_factors = ['TEMP', 'RAIN', 'WSPM', 'PRES', 'DEWP']
    correlation_pm2_5_weather = data_clean[weather_factors + ['PM2.5']].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_pm2_5_weather, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Korelasi PM2.5 dengan Faktor Cuaca', fontsize=14)
    st.pyplot(fig)

# Analisis 4: Distribusi PM2.5 Berdasarkan Kategori
elif analysis_option == 'Distribusi PM2.5 Berdasarkan Kategori':
    st.subheader('Distribusi PM2.5 berdasarkan Kategori')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='PM2.5_Kategori', data=data_clean, ax=ax, palette='coolwarm')
    ax.set_title('Distribusi PM2.5 berdasarkan Kategori')
    ax.set_xlabel('Kategori PM2.5')
    ax.set_ylabel('Jumlah Data')
    st.pyplot(fig)
