import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# JANGAN tambahkan argumen lain di dalam kurung ini
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Membaca data menggunakan pengaturan otomatis dari Secrets
    df = conn.read()
    
    st.subheader("Daftar Tabungan")
    st.dataframe(df, use_container_width=True)
    st.success("Alhamdulillah, koneksi berhasil!")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
