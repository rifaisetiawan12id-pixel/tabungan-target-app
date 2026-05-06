import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Judul Aplikasi
st.title("🎯 Tabungan Target")

# 1. Inisialisasi Koneksi (Nama "gsheets" harus sama dengan di Secrets)
conn = st.connection("gsheets", type=GSheetsConnection)

# 2. Ambil Data dari Google Sheets
try:
    # Mengambil data dari Sheet1
    data = conn.read(worksheet="Sheet1", ttl="0")
    
    # Tampilkan Data Ringkasan
    st.subheader("Daftar Tabungan")
    st.dataframe(data, use_container_width=True)

    # 3. Form Input Data Baru
    with st.expander("➕ Tambah Target Baru"):
        with st.form("input_form"):
            nama_barang = st.text_input("Nama Barang")
            harga_target = st.number_input("Harga Target (Rp)", min_value=0)
            terkumpul = st.number_input("Terkumpul (Rp)", min_value=0)
            deadline = st.date_input("Deadline")
            
            submit = st.form_submit_button("Simpan ke Google Sheets")
            
            if submit:
                if nama_barang:
                    # Buat DataFrame baru untuk baris yang ditambah
                    new_row = pd.DataFrame([{
                        "Nama_Barang": nama_barang,
                        "Harga_Target": harga_target,
                        "Terkumpul": terkumpul,
                        "Deadline": str(deadline)
                    }])
                    
                    # Gabungkan data lama dan baru
                    updated_df = pd.concat([data, new_row], ignore_index=True)
                    
                    # Update ke Google Sheets
                    conn.update(worksheet="Sheet1", data=updated_df)
                    st.success(f"Berhasil menambah target: {nama_barang}!")
                    st.rerun()
                else:
                    st.error("Nama Barang tidak boleh kosong!")

except Exception as e:
    st.error(f"Waduh, ada masalah koneksi: {e}")
    st.info("Pastikan email Service Account sudah di-invite sebagai Editor di Google Sheets kamu.")
