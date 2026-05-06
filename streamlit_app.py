import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🎯 Tabungan Target")

# Membuat koneksi otomatis dari secrets
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Membaca data
    df = conn.read()
    st.dataframe(df)
    st.success("Koneksi berhasil!")
except Exception as e:
    st.error(f"Gagal membaca data: {e}")
