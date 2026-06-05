# Burnout Detection & Lifestyle Analysis Dashboard

Dashboard interaktif berbasis web yang dibangun menggunakan **Streamlit** untuk mendeteksi tingkat burnout, menganalisis faktor penyebab stres, pola tidur, aktivitas harian pengguna, serta prediksiresiko burnout. Proyek ini dilengkapi dengan analisis data eksploratif (EDA) melalui Jupyter Notebook.

## 🚀 Fitur Utama
* **Burnout Metrics & Preview**: Ringkasan data responden terkait waktu tidur dan screen time.
* **Multipage Dashboard**:
  * Faktor-faktor pemicu burnout.
  * Analisis mendalam mengenai waktu tidur.
  * Analisis gaya hidup responden.
* **Notebook Analisis**: Prosedur eksperimen data yang terdokumentasi di folder `notebook/`.

## 🗂️ Struktur Direktori
```
DASHBOARD/
├── data/
│   ├── df.csv
├── notebook/
│   ├── notebook.ipynb
│   ├── order_clean.csv
├── pages/
│   ├── 01_Burnout_Factors.py
│   ├── 02_Sleep_Analysis.py
|   ├── 03_Lifestyle_Analysis.py
├── app.py
├── README.md
└── requirements.txt
```

## 🚀 Panduan Menjalankan Aplikasi
### Setup Environment env
Langkah pertama, Clone Tepositori ini atau mengunduhnya dalam bentuk zip

selanjutnya membuat environment:
```
python3 -m venv env

# Windows 
.\venv\Scripts\activate

# linux
source env/bin/activate
```

### Instalasi Library
Instal library yang dibutuhkan menggunakan pip:
```
pip install -r requirements.txt
```

### Menjalankan Dashboard Menggunakan steamlit app
Pergi ke directori dashboard kemudian ketik kode berikut di terminal:
```
streamlit run app.py
```
atau
```
python -m streamlit run app.py
```
Aplikasi akan berjalan

## 📜 Lisensi

Proyek ini didistribusikan di bawah MIT License. Kamu bebas untuk menggunakan, menyalin, dan memodifikasi kode ini untuk keperluan pendidikan maupun pengembangan portofolio pribadi.