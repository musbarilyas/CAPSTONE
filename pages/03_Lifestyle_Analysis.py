import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/df.csv")

st.title("💻 Lifestyle Analysis")

st.subheader("Screen Time Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["screen_time"],
    bins=15,
    kde=True,
    ax=ax
)

st.pyplot(fig)

st.info("""
Visualisasi ini menunjukkan distribusi durasi screen time responden setiap hari.
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

st.subheader("Caffeine Intake vs Stress Score")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="caffeine_intake",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.subheader("Daily Activity Hours vs Stress Score")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="daily_activity_hours",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.subheader("Key Findings")

st.success("""
Faktor gaya hidup seperti screen time, konsumsi kafein, dan durasi aktivitas harian dapat memengaruhi tingkat stres responden.

Temuan ini dapat digunakan untuk membantu identifikasi pola perilaku yang berpotensi meningkatkan risiko burnout.
""")
