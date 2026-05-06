import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🎯 Tabungan Target")

# Membuat koneksi
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Membaca data dari Google Sheets
    df = conn.read()
    st.write("### Data Tabungan Anda:")
    st.dataframe(df)
    st.success("Koneksi berhasil!")
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca data: {e}")
