import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = '../PRSA_Data_Aotizhongxin_20130301-20170228.csv'
data = pd.read_csv(file_path)

data_clean = data.drop_duplicates()
data_clean['datetime'] = pd.to_datetime(data_clean[['year', 'month', 'day', 'hour']])

st.title('Dashboard Kualitas Udara dan Cuaca Aotizhongxin')

analysis_option = st.sidebar.selectbox('Pilih Analisis', ['Distribusi Polusi Udara', 'Tren PM2.5 Seiring Waktu', 'Korelasi Cuaca dan PM2.5'])

# Analisis 1: Distribusi Polusi Udara
if analysis_option == 'Distribusi Polusi Udara':
    st.subheader('Distribusi PM2.5 dan PM10')
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

# Analisis 2: Tren PM2.5 Seiring Waktu
elif analysis_option == 'Tren PM2.5 Seiring Waktu':
    st.subheader('Tren Rata-rata PM2.5 Seiring Waktu')
    fig, ax = plt.subplots(figsize=(12, 6))
    data_clean.groupby('datetime')['PM2.5'].mean().plot(ax=ax)
    ax.set_title('Rata-rata Konsentrasi PM2.5 Seiring Waktu')
    ax.set_xlabel('Waktu')
    ax.set_ylabel('Rata-rata PM2.5')
    st.pyplot(fig)

# Analisis 3: Korelasi Cuaca dan PM2.5
elif analysis_option == 'Korelasi Cuaca dan PM2.5':
    st.subheader('Korelasi PM2.5 dengan Faktor Cuaca')
    
    weather_factors = ['TEMP', 'RAIN', 'WSPM', 'PRES', 'DEWP']
    correlation_pm2_5_weather = data_clean[weather_factors + ['PM2.5']].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_pm2_5_weather, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Korelasi PM2.5 dengan Faktor Cuaca')
    st.pyplot(fig)