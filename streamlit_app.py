import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# Koneksi menggunakan Secrets
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Ambil data dari Sheet1
    data = conn.read(worksheet="Sheet1")
    
    st.subheader("Daftar Tabungan")
    st.dataframe(data, use_container_width=True)
    st.success("Koneksi ke Google Sheets Berhasil!")

except Exception as e:
    st.error(f"Error Koneksi: {e}")
