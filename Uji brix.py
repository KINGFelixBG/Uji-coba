import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Judul aplikasi
st.title(" Uji Brix pada Bahan Pangan ")

# Deskripsi aplikasi
st.write("""
Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu.
""")

# Sidebar untuk input
with st.sidebar:
    st.header("Input Parameter")
    brix_awal = st.number_input("Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)
    show_dark_mode = st.checkbox("Aktifkan Mode Gelap")

# Terapkan mode gelap jika dipilih
if show_dark_mode:
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: red; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#F0F8FF"
secondaryBackgroundColor = "#E6F0FA"
textColor = "#000000"
font = "sans serif"

# Penjelasan tentang uji Brix
with st.expander("📘 Apa itu Uji Brix?"):
    st.markdown("""
**Pengertian:**

Derajat Brix (°Bx) adalah satuan yang menunjukkan jumlah zat padat terlarut, terutama gula (sukrosa), dalam 100 gram larutan. Sebagai contoh, larutan dengan 10 °Bx berarti mengandung 10 gram gula dalam setiap 100 gram larutan. Uji Brix digunakan untuk mengukur konsentrasi gula dalam berbagai produk pangan cair seperti jus buah, madu, sirup, dan nira tebu.

**Rumus Koreksi Suhu:**

Karena indeks bias dipengaruhi oleh suhu, penting untuk melakukan koreksi suhu jika alat tidak memiliki kompensasi suhu otomatis. Rumus koreksi suhu sederhana:



Dengan:

**Brix_awal**: Nilai Brix yang dibaca langsung dari refraktometer.
**Suhu_sample**: Suhu aktual larutan saat pengukuran.
**Suhu_referensi**: Suhu standar, biasanya 20°C.
**Faktor_koreksi**: Nilai koreksi per derajat Celsius, umumnya 0.03 °Bx/°C.

**Alat yang Digunakan:**

1. **Refraktometer**: Alat utama untuk mengukur Brix, tersedia dalam bentuk analog dan digital.
2. **Hidrometer**: Mengukur berat jenis larutan, yang dapat dikonversi ke nilai Brix menggunakan tabel.
3. **Termometer**: Digunakan untuk mengukur suhu larutan saat pengujian, penting untuk koreksi suhu.
4. **Piknometer**: Alat laboratorium untuk mengukur massa jenis larutan dengan presisi tinggi.

**Langkah-Langkah Pengukuran:**

1. **Kalibrasi Alat**: Teteskan air suling pada prisma refraktometer untuk memastikan pembacaan menunjukkan 0 °Bx.
2. **Persiapan Sampel**: Ambil sampel larutan yang akan diuji.
3. **Pengukuran**: Teteskan sampel pada prisma refraktometer dan baca nilai Brix yang ditunjukkan.
4. **Koreksi Suhu**: Jika alat tidak memiliki kompensasi suhu otomatis, lakukan koreksi menggunakan rumus yang telah disebutkan.
    """)



# Tombol untuk menghitung koreksi Brix
if st.button("Hitung Koreksi Brix"):
    suhu_referensi = 20.0
    faktor_koreksi = 0.03

    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    st.success(f"Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {faktor_koreksi}) = {brix_terkoreksi:.2f} °Bx")

    # Penilaian kualitas bahan pangan
    if brix_terkoreksi < 10:
        kualitas = "Rendah (contoh: buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar industri untuk buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, atau buah sangat manis)"

    st.info(f"Kategori Kadar Gula: {kualitas}")

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")
