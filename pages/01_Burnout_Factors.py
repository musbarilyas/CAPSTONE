import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/df.csv")

st.title("📊 Burnout Factors Analysis")

st.write("""
Halaman ini digunakan untuk menganalisis faktor-faktor yang berhubungan dengan tingkat stres dan burnout responden.
""")

st.subheader("Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.subheader("Sleep Hours vs Stress Score")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="sleep_hours",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.info("""
Grafik ini digunakan untuk melihat apakah durasi tidur memiliki hubungan dengan tingkat stres.
""")

st.subheader("Screen Time vs Stress Score")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="screen_time",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.info("""
Visualisasi ini membantu melihat apakah penggunaan perangkat digital yang tinggi berasosiasi dengan peningkatan tingkat stres.
""")

st.subheader("Caffeine Intake vs Stress Score")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="caffeine_intake",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.subheader("Key Findings")

st.success("""
Beberapa variabel seperti sleep_hours, screen_time, dan caffeine_intake menunjukkan hubungan dengan tingkat stres responden.

Temuan ini dapat digunakan sebagai dasar pengembangan model prediksi burnout dan rekomendasi gaya hidup yang lebih sehat.
""")
