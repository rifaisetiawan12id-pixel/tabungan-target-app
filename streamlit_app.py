import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import json

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# --- TRIK BARU: Membaca Secrets Secara Manual ---
try:
    # Mengambil data dari Secrets Streamlit
    creds_dict = {
        "type": st.secrets["connections"]["gsheets"]["type"],
        "project_id": st.secrets["connections"]["gsheets"]["project_id"],
        "private_key_id": st.secrets["connections"]["gsheets"]["private_key_id"],
        "private_key": st.secrets["connections"]["gsheets"]["private_key"],
        "client_email": st.secrets["connections"]["gsheets"]["client_email"],
        "client_id": st.secrets["connections"]["gsheets"]["client_id"],
        "auth_uri": st.secrets["connections"]["gsheets"]["auth_uri"],
        "token_uri": st.secrets["connections"]["gsheets"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["connections"]["gsheets"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["connections"]["gsheets"]["client_x509_cert_url"],
    }
    
    # Koneksi menggunakan kredensial yang sudah dibaca manual
    conn = st.connection("gsheets", type=GSheetsConnection, **creds_dict)
    
    # Ambil data dari link spreadsheet kamu langsung
    url = "https://docs.google.com/spreadsheets/d/1DeucSufj0CH87BKRg1YqHosfdtCO-olHkgktAT9QBUk/edit"
    data = conn.read(spreadsheet=url, worksheet="Sheet1")
    
    st.subheader("Daftar Tabungan")
    st.dataframe(data, use_container_width=True)
    st.success("Mantap! Koneksi Berhasil.")

except Exception as e:
    st.error(f"Gagal memuat konfigurasi: {e}")
    st.info("Pastikan di bagian Secrets kamu sudah menuliskan [connections.gsheets] dengan benar.")
