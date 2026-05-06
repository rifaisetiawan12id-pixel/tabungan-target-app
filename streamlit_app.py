import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# Fungsi untuk membersihkan format private key yang sering error di Streamlit Cloud
def fix_key(key):
    return key.replace("\\n", "\n")

try:
    # 1. Ambil kredensial dari secrets secara manual agar lebih aman
    creds = dict(st.secrets["connections"]["gsheets"])
    creds["private_key"] = fix_key(creds["private_key"])
    
    # 2. Buat koneksi dengan kredensial yang sudah diperbaiki
    conn = st.connection("gsheets", type=GSheetsConnection, **creds)
    
    # 3. Baca data (Pastikan Sheet1 adalah nama tab di Google Sheets kamu)
    df = conn.read(worksheet="Sheet1")
    
    st.subheader("Daftar Tabungan")
    st.dataframe(df, use_container_width=True)
    st.success("Koneksi Berhasil!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Tips: Pastikan di bagian Secrets, isi private_key diawali dengan '-----BEGIN PRIVATE KEY-----'")
