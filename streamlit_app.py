import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Tabungan Target", page_icon="🎯")
st.title("🎯 Tabungan Target")

# 1. Ambil secrets dan perbaiki format private_key secara manual
raw_creds = st.secrets["connections"]["gsheets"]
creds_dict = dict(raw_creds)
creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

try:
    # 2. Buat koneksi (Kunci perbaikannya: jangan tulis type=GSheetsConnection di sini)
    # Kita masukkan semua data lewat **creds_dict
    conn = st.connection("gsheets", type=GSheetsConnection, **creds_dict)
    
    # 3. Baca data
    df = conn.read(spreadsheet=creds_dict.get("spreadsheet"), worksheet="Sheet1")
    
    st.subheader("Daftar Tabungan")
    st.dataframe(df, use_container_width=True)
    st.success("Alhamdulillah, Koneksi Berhasil!")

except Exception as e:
    st.error(f"Waduh, masih ada error: {e}")
