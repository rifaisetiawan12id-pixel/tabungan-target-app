import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("🎯 Tabungan Target")

# CARA MANUAL: Masukkan data langsung ke sini
# Ganti URL di bawah dengan link Google Sheets kamu yang asli
url = "https://docs.google.com/spreadsheets/d/1DeucSufj0CH87BKRg1YqHosfdtCO-olHkgktAT9QBUk/edit"

try:
    # Kita pakai koneksi tanpa label gsheets dulu untuk tes
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # Ambil data langsung menggunakan URL
    data = conn.read(spreadsheet=url, worksheet="Sheet1")
    
    st.subheader("Daftar Tabungan")
    st.dataframe(data, use_container_width=True)
    
    st.success("Koneksi Berhasil!")

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Coba cek apakah file requirements.txt kamu sudah ada 'st-gsheets-connection'?")
