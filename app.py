import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load

st.set_page_config(page_title="Burnout Detection Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/df.csv")

@st.cache_resource
def load_model():
    model = load("model/burnout_model.joblib")
    le    = load("model/label_encoder.joblib")
    return model, le

df = load_data()
model, le = load_model()

st.sidebar.title("Burnout Dashboard")
st.sidebar.divider()
st.sidebar.subheader("Filter Data")

age_range = st.sidebar.slider("Rentang Umur", int(df["age"].min()), int(df["age"].max()), (int(df["age"].min()), int(df["age"].max())))
df_filtered = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]
st.sidebar.info(f"Menampilkan **{len(df_filtered):,}** dari **{len(df):,}** responden (umur {age_range[0]}-{age_range[1]} tahun)")

st.title("Burnout Detection Dashboard")
st.markdown(f"Menampilkan data untuk rentang umur **{age_range[0]}-{age_range[1]} tahun** · {len(df_filtered):,} responden")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Responden", f"{len(df_filtered):,}")
col2.metric("Rata-rata Jam Tidur", f"{df_filtered['sleep_hours'].mean():.2f} jam")
col3.metric("Rata-rata Screen Time", f"{df_filtered['screen_time'].mean():.2f} jam")
col4.metric("Rata-rata Jam Aktivitas",f"{df_filtered['daily_activity_hours'].mean():.2f} jam")

st.divider()
st.subheader("Dataset Preview")
st.dataframe(df_filtered, use_container_width=True)
st.divider()

col_left, col_right = st.columns(2)
with col_left:
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["sleep_hours"], kde=True, ax=ax)
    ax.set_title("Distribusi Jam Tidur")
    st.pyplot(fig); plt.close()

    fig, ax = plt.subplots()
    sns.countplot(data=df_filtered, x="burnout_general", order=["Low","Medium","High"],
                  palette={"Low":"green","Medium":"orange","High":"red"}, ax=ax)
    ax.set_title("Distribusi Burnout Level")
    st.pyplot(fig); plt.close()

with col_right:
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["stress_score"], bins=20, kde=True, ax=ax, color="coral")
    ax.set_title("Distribusi Stress Score")
    st.pyplot(fig); plt.close()

    counts = df_filtered["burnout_general"].value_counts().reindex(["Low","Medium","High"])
    fig, ax = plt.subplots()
    ax.pie(counts, labels=["Low","Medium","High"], colors=["green","orange","red"],
           autopct="%1.1f%%", startangle=90)
    st.pyplot(fig); plt.close()

st.info("Mayoritas responden memiliki tingkat burnout pada kategori medium. Durasi tidur rata-rata berada di bawah rekomendasi ideal 7-9 jam.")
st.divider()

st.title("Analisis Data")
st.markdown(f"Rentang umur: **{age_range[0]}-{age_range[1]} tahun** · {len(df_filtered):,} responden")
st.subheader("Distribusi Fitur Kesehatan Universal")

fitur_pilihan = st.selectbox("Pilih Fitur", [
    "sleep_hours", "daily_activity_hours", "exercise_hours",
    "screen_time", "caffeine_intake", "stress_score"
])

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df_filtered[fitur_pilihan], kde=True, ax=ax)
ax.set_title(f"Distribusi {fitur_pilihan}")
st.pyplot(fig); plt.close()

col1, col2, col3 = st.columns(3)
col1.metric("Mean",   f"{df_filtered[fitur_pilihan].mean():.2f}")
col2.metric("Median", f"{df_filtered[fitur_pilihan].median():.2f}")
col3.metric("Std",    f"{df_filtered[fitur_pilihan].std():.2f}")

st.divider()
st.title("Prediksi Burnout")
st.markdown("Masukkan data kesehatan kamu untuk memprediksi risiko burnout.")
st.divider()

col_input, col_result = st.columns(2)

with col_input:
    st.subheader("Input Data")
    daily_activity   = st.slider("Jam Aktivitas Harian",4.0, 14.0, 8.0,  0.5)
    sleep_hours      = st.slider("Jam Tidur per Malam",  4.0,  9.0, 7.0,  0.5)
    exercise_hours   = st.slider("Jam Olahraga per Hari", 0.0,  2.0, 1.0,  0.1)
    screen_time      = st.slider("Screen Time per Hari (jam)",5.0, 19.0, 10.0, 0.5)
    caffeine_intake  = st.slider("Konsumsi Kafein (cangkir)", 0, 7, 2)
    age              = st.number_input("Usia",15, 65, 25)
    prediksi_btn     = st.button("Prediksi Sekarang",use_container_width=True)

with col_result:
    st.subheader("Hasil Prediksi")

    if prediksi_btn:
        input_data = pd.DataFrame([{
            "daily_activity_hours": daily_activity,
            "sleep_hours"         : sleep_hours,
            "exercise_hours"      : exercise_hours,
            "screen_time"         : screen_time,
            "caffeine_intake"     : caffeine_intake,
            "age"                 : age,
        }])

        pred_label = le.inverse_transform(model.predict(input_data))[0]
        pred_proba = model.predict_proba(input_data)[0]

        if pred_label == "Low":
            pesan = "Risiko burnout kamu rendah."
            st.success(f"Hasil: {pred_label} Burnout Risk")
        elif pred_label == "Medium":
            pesan = "Risiko burnout kamu sedang."
            st.warning(f"Hasil: {pred_label} Burnout Risk")
        else:
            pesan = "Risiko burnout kamu tinggi. Jangan lupa untuk kurangi beban dan beristirahat."
            st.error(f"Hasil: {pred_label} Burnout Risk")

        st.write(pesan)
        st.divider()

        st.markdown("*Probabilitas per Kategori:*")
        for label, prob in zip(le.classes_, pred_proba):
            st.progress(float(prob), text=f"{label}: {prob*100:.1f}%")

        st.divider()
        st.markdown("**Faktor yang Berkontribusi:**")
        faktor = []
        if daily_activity>9:faktor.append("Jam aktivitas melebihi 11 jam/hari")
        if sleep_hours<7: faktor.append("Jam tidur kurang dari 7 jam")
        if exercise_hours<0.35:faktor.append("Olahraga kurang dari 0.5 jam/hari")
        if caffeine_intake >4:faktor.append("Konsumsi kafein melebihi 4 cangkir")
        if screen_time >10:faktor.append("Screen time melebihi 10 jam")

        if faktor:
            for f in faktor:
                st.markdown(f"- {f}")
        else:
            st.markdown("Tidak ada faktor risiko yang terdeteksi.")
