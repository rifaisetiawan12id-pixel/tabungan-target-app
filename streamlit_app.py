import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🎯 Tabungan Target")

# Koneksi sederhana
conn = st.connection("gsheets", type=GSheetsConnection)

# Coba baca data
try:
    df = conn.read()
    st.write("Koneksi Berhasil! Berikut datanya:")
    st.dataframe(df)
except Exception as e:
    st.error(f"Waduh, koneksi gagal: {e}")
    st.info("Coba cek kembali isi Secrets di Advanced Settings.")
