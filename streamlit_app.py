import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# --- CARA MANUAL TOTAL ---
try:
    # Kita ambil langsung per key dari st.secrets
    gsheets_conf = st.secrets["connections"]["gsheets"]
    
    # Buat dictionary kredensial
    creds = {
        "type": gsheets_conf["type"],
        "project_id": gsheets_conf["project_id"],
        "private_key_id": gsheets_conf["private_key_id"],
        "private_key": gsheets_conf["private_key"].replace("\\n", "\n"),
        "client_email": gsheets_conf["client_email"],
        "client_id": gsheets_conf["client_id"],
        "auth_uri": gsheets_conf["auth_uri"],
        "token_uri": gsheets_conf["token_uri"],
        "auth_provider_x509_cert_url": gsheets_conf["auth_provider_x509_cert_url"],
        "client_x509_cert_url": gsheets_conf["client_x509_cert_url"],
    }
    
    # Koneksi menggunakan kredensial manual
    conn = st.connection("gsheets", type=GSheetsConnection, **creds)
    
    # Baca data menggunakan link spreadsheet langsung
    url = gsheets_conf["spreadsheet"]
    df = conn.read(spreadsheet=url)
    
    st.subheader("Daftar Tabungan")
    st.dataframe(df, use_container_width=True)
    st.success("Koneksi Manual Berhasil!")

except KeyError as e:
    st.error(f"Data tidak ditemukan di Secrets: {e}")
    st.info("Pastikan di Secrets ada tulisan [connections.gsheets] di baris paling atas.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
