import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Menyediakan path file
file_path = 'data/data.csv'
data = pd.read_csv(file_path)

# Data cleaning
data_clean = data.drop_duplicates()
data_clean['datetime'] = pd.to_datetime(data_clean[['year', 'month', 'day', 'hour']])

# Menambahkan kategori binning pada PM2.5
bins = [0, 50, 100, 150, np.inf]
labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
data_clean['PM2.5_Kategori'] = pd.cut(data_clean['PM2.5'], bins=bins, labels=labels)

# Dashboard Title
st.title('Dashboard Kualitas Udara dan Cuaca Aotizhongxin')

# Dokumentasi di Sidebar
st.sidebar.write("### Deskripsi Dashboard")
st.sidebar.write("""
Pada dashboard ini, kita akan melakukan analisis terhadap data kualitas udara dan cuaca yang diambil dari stasiun Aotizhongxin.
Berikut adalah beberapa analisis yang bisa dipilih:
1. **Distribusi Polusi Udara**: Menganalisis distribusi PM2.5 dan PM10 untuk melihat bagaimana polusi udara tersebar dalam dataset.
2. **Tren PM2.5 Seiring Waktu**: Melihat apakah ada tren perubahan dalam kualitas udara seiring waktu.
3. **Korelasi Cuaca dan PM2.5**: Menganalisis hubungan antara faktor cuaca (suhu, curah hujan, kecepatan angin) dan kualitas udara.
4. **Distribusi PM2.5 Berdasarkan Kategori**: Melihat distribusi PM2.5 berdasarkan kategori rendah, sedang, tinggi, dan sangat tinggi.
""")

analysis_option = st.sidebar.selectbox('Pilih Analisis', ['Distribusi Polusi Udara', 'Tren PM2.5 Seiring Waktu', 'Korelasi Cuaca dan PM2.5', 'Distribusi PM2.5 Berdasarkan Kategori'])

# Analisis 1: Distribusi Polusi Udara
if analysis_option == 'Distribusi Polusi Udara':
    st.subheader('Distribusi PM2.5 dan PM10')
    st.write("Pada analisis ini, kita akan melihat distribusi polusi udara berdasarkan PM2.5 dan PM10.")
    col1, col2 = st.columns(2)

    # PM2.5 Distribution
    with col1:
        st.write("Distribusi PM2.5")
        fig, ax = plt.subplots()
        sns.histplot(data_clean['PM2.5'], kde=True, color='skyblue', ax=ax)
        st.pyplot(fig)

    # PM10 Distribution
    with col2:
        st.write("Distribusi PM10")
        fig, ax = plt.subplots()
        sns.histplot(data_clean['PM10'], kde=True, color='salmon', ax=ax)
        st.pyplot(fig)
