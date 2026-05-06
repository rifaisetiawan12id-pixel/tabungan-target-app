import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# 1. Konfigurasi Halaman & Judul
st.set_page_config(page_title="Saving Goals Tracker", page_icon="🎯")
st.title("🎯 Tabungan Target (Saving Goals)")

# 2. Koneksi ke Google Sheets (Database di Drive)
conn = st.connection("gsheets", type=GSheetsConnection)

def load_data():
    return conn.read(ttl=0)

data = load_data()

# 3. Logika & Tampilan Dashboard (Visualisasi)
st.subheader("📊 Progres Tabungan")
if not data.empty:
    for index, row in data.iterrows():
        with st.container():
            target = float(row['Harga_Target'])
            terkumpul = float(row['Terkumpul'])
            persen = min(terkumpul / target, 1.0)
            sisa = target - terkumpul
            
            # Hitung sisa hari
            deadline = datetime.strptime(str(row['Deadline']), "%Y-%m-%d")
            hari_tersisa = (deadline - datetime.now()).days
            
            st.write(f"### {row['Nama_Barang']}")
            st.progress(persen)
            st.write(f"Progres: {persen*100:.1f}% (Rp {terkumpul:,.0f} / Rp {target:,.0f})")
            
            if sisa > 0:
                if hari_tersisa > 0:
                    harian = sisa / hari_tersisa
                    st.info(f"💡 Untuk mencapai target dalam {hari_tersisa} hari, kamu harus menabung **Rp {harian:,.0f}/hari**.")
                else:
                    st.warning("⚠️ Waktu sudah lewat!")
            else:
                st.success("✅ Target Tercapai!")
            st.divider()

# 4. Fungsi Tambah Data (Create)
with st.expander("➕ Tambah Target Baru"):
    with st.form("tambah_form"):
        nama = st.text_input("Nama Barang")
        harga = st.number_input("Harga Target (Rp)", min_value=0)
        awal = st.number_input("Nominal Awal (Rp)", min_value=0)
        tgl = st.date_input("Deadline")
        submit = st.form_submit_button("Simpan Target")
        
        if submit and nama:
            new_row = pd.DataFrame([{
                "Nama_Barang": nama, "Harga_Target": harga, 
                "Terkumpul": awal, "Deadline": str(tgl)
            }])
            updated_df = pd.concat([data, new_row], ignore_index=True)
            conn.update(data=updated_df)
            st.success("Berhasil disimpan!")
            st.rerun()

# 5. Fungsi Update Tabungan (Update)
if not data.empty:
    with st.expander("💰 Isi Tabungan"):
        pilihan = st.selectbox("Pilih Target", data['Nama_Barang'])
        tambah_uang = st.number_input("Masukkan Jumlah (Rp)", min_value=0)
        if st.button("Update Saldo"):
            data.loc[data['Nama_Barang'] == pilihan, 'Terkumpul'] += tambah_uang
            conn.update(data=data)
            st.success("Saldo diperbarui!")
            st.rerun()
