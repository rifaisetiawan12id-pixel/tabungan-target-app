import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Tabungan Target", layout="centered")
st.title("🎯 Tabungan Target")

# Masukkan detail JSON kamu di sini secara manual
# Ini untuk menghindari error 'multiple values' dari menu Secrets
creds = {
    "type": "service_account",
    "project_id": "aplikasi-tabungan-target",
    "private_key_id": "a2b70a22d9e3d0172073001fb082cda9476c7b59",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDP4Gelc9Sv9jWY\nsXElZtQpir8u13e0+5Fpgnq5NL8/ANEKrlGYMenZDSZqFyjTdDMDSZH171CtOKVQ\nXtjmkl0EOIJoqcQsKuuqQAfHy9IRTYgsqxSDrGpxoy2EME2IfO+DCxBV5uqsRknh\n1Z6HMWIp6lqBp0S9+5B5/abOK3/XrsAIPS5mlSFaGmkpdxT++ebqOKbojWfo2C+C\ni2cTK+rMgGugi8Gv0ZBpmBYqY4GuMLxq2iUu6q8O6l/sE0iDLTh98fH9J6JX40Pl\n8Z9DP2cTtdYCH1OTSOebMwqAKN8UwNNeyL3ErpFVkoC7ODsYg7ywmFgZ3tuklFtz\ny3PeeEYlAgMBAAECggEAIE7ilQC0bve/e0Ci0vsRIPa/QY67/G03+7PLkqLr0WU1\nWClhJZwmWfV1AbqhPgIalpl13cko2w9JhD0FjYp0ef41aIJwKqQuFfsXKnqXZtiL\nwFODn/ZpYcmIfrnKJxsx14Zd7tfxo75V58tddOocNWMG141RfgyN9yPQ68yvdSwc\nEFI54zuvLe1k3f2SdBDnVY3smMOv20mzJ2xSKO3lRkmJS/aFR3C7CZVp0YAZIhmD\nFUDpKC8jeKWJhQqZ2fnStJmiJEz3aio051dM+HHfhdSlAptJ9DYBhaVLM0PHLcmo\nhVtnheWrADaNV6wvgUjW1/qZla2Lc3NK5H5uD9fImQKBgQD79sDnaqaxn/Zfb1il\Sq/AtN90SmUAtfI+6VPvyGqAQ4ZX7pJZhLHdUhmeJ0UBNLyahlL3lPb2pTabuDAw\nSU3wDCu9v64NdTl9SfBPlZpLP092KNrbnInZEqmzyRo6b5QOIAB9F86iXVHffd5b\nOAifW9EoQpb8RxGyRMrlikh1uQKBgQDTNNv/d//X5RqjF6jj11D4GK11h7NUcZ9y\n96R9053hCIURQ3seirevxCwt1XeFJoeJcN2M6p2hDpnBdhDgmr5ZA/CsSlC0EOlS\nwcZt01x2T2jvior8A3CHVpuaEgiRkUehTFS0u4w2EwyiXXBqHCajil0F2VnaIAjt\nFg/d8AKJzQKBgQCqnap+ie+as/EHKsTiGLLuUQxHGOFQG+SPyTv3UMUdWZwtCvW6\n/Gncrm1+dKT7bhSQpoij8hFRbwqNY6nt6JWICRXNhXB82HY3asv5eBpk/df28S9S\nKqwFe+fCQFksXMXq0qzCCE76DysTpY3eQxFDp8737i+DYTSQfJjP2lW6sQKBgQCW\nlzHlTSJWRTxg3RXGnldVDgNfsYnjw7/0sS3PqXsAYJrAXGUEudOOt0joxTOa9IXf\nMWJGf2I027w1fIE8JBlkTrLjpXk1anlyUEezNujOUoB3i0jdt3YciVwY1pLVd8ii\n8VHUK4UlaR+xBP6KKdhC8vywlvDB3eV/ZiOaEu88YQKBgCK9tHeBbrcwBjuBIwEJ\noLo5pSr27fmIjTZ8i01r4tB9Pt4DpTeNsjm27H9qA58Qct52/mSJwsTk0wsbD8K1\nj6eho3LZ6hZKBM+Yf4JWI/Q8LlJZSKcdVH++K9RcSqbGS47wKqgtYwGCL6w/cC99\nKEb1p8vzP0gYEQ3adUV5Fv8Z\n-----END PRIVATE KEY-----\n",
    "client_email": "admin-tabungan@aplikasi-tabungan-target.iam.gserviceaccount.com"
}

# Link Spreadsheet kamu
url = "https://docs.google.com/spreadsheets/d/1DeucSufj0CH87BKRg1YqHosfdtCO-olHkgktAT9QBUk/edit"

# Membuat koneksi TANPA menyebutkan type=GSheetsConnection lagi
# agar tidak terjadi tabrakan argumen
try:
    conn = st.connection("gsheets", **creds)
    
    with st.form("input_form"):
        nama = st.text_input("Keperluan Tabungan")
        jumlah = st.number_input("Nominal (Rp)", step=1000)
        tgl = st.date_input("Tanggal")
        submit = st.form_submit_button("Simpan Data")

    if submit:
        df = conn.read(spreadsheet=url)
        new_row = {"Nama Target": nama, "Nominal": jumlah, "Tanggal": tgl.strftime("%d/%m/%Y")}
        df_baru = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        conn.update(spreadsheet=url, data=df_baru)
        st.success("Data berhasil disimpan ke Android!")

    st.divider()
    st.subheader("Riwayat")
    st.dataframe(conn.read(spreadsheet=url), use_container_width=True)

except Exception as e:
    st.error(f"Error Sistem: {e}")
