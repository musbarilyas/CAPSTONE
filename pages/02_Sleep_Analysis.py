import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/df.csv")

st.title("😴 Sleep Analysis")

st.subheader("Sleep Hours Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["sleep_hours"],
    bins=15,
    kde=True,
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

bins = [0,4,6,8,24]
labels = [
    "Very Low Sleep",
    "Low Sleep",
    "Healthy Sleep",
    "High Sleep"
]

df["sleep_category"] = pd.cut(
    df["sleep_hours"],
    bins=bins,
    labels=labels
)

st.subheader("Average Stress Score by Sleep Category")

sleep_stress = (
    df.groupby("sleep_category")["stress_score"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=sleep_stress,
    x="sleep_category",
    y="stress_score",
    ax=ax
)

st.pyplot(fig)

st.success("""
Analisis menunjukkan hubungan antara kualitas istirahat dan tingkat stres.

Kategori tidur yang lebih rendah cenderung memiliki skor stres yang lebih tinggi dibandingkan kelompok dengan durasi tidur yang lebih sehat.
""")
