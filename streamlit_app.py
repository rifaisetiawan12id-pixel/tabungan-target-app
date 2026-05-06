import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# 1. Koneksi Paling Sederhana
# Kita biarkan Streamlit mengambil semua data otomatis dari Secrets
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # 2. Baca Data
    # Ganti link di bawah dengan link spreadsheet kamu jika berbeda
    url = "https://docs.google.com/spreadsheets/d/1DeucSufj0CH87BKRg1YqHosfdtCO-olHkgktAT9QBUk/edit"
    df = conn.read(spreadsheet=url, worksheet="Sheet1")
    
    # 3. Tampilkan Data
    st.subheader("Daftar Tabungan Kamu")
    st.dataframe(df, use_container_width=True)
    
    st.success("Koneksi Berhasil! Data sudah muncul.")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Cek kembali apakah Secrets sudah di-Save dan email Service Account sudah di-invite ke Google Sheets.")
