import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# HANYA GUNAKAN INI:
# Jangan tambahkan argumen lain seperti spreadsheet=... atau **creds
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Ambil data otomatis menggunakan settingan dari Secrets
    df = conn.read()
    
    st.subheader("Daftar Tabungan")
    st.dataframe(df, use_container_width=True)
    st.success("Alhamdulillah, akhirnya berhasil!")

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Pastikan settingan di Secrets sudah benar.")
