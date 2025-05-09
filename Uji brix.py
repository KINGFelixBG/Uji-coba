import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Judul aplikasi
st.title("😚 Uji Brix pada Bahan Pangan 🍕🍟")

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
            body { background-color: #1e1e1e; color: white; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# Penjelasan tentang uji Brix
with st.expander("📘 Apa itu Uji Brix?"):
    st.markdown("""
**Pengertian:**

Derajat Brix (°Bx) adalah satuan yang menunjukkan jumlah zat padat terlarut, terutama gula (sukrosa), dalam 100 gram larutan. Sebagai contoh, larutan dengan 10 °Bx berarti mengandung 10 gram gula dalam setiap 100 gram larutan. Uji Brix digunakan untuk mengukur konsentrasi gula dalam berbagai produk pangan cair seperti jus buah, madu, sirup, dan nira tebu. [Referensi](https://www.saka.co.id/news-detail/pengukuran-brix-dan-indeks-bias-di-lab-komersial-pangan)

**Rumus Koreksi Suhu:**

Karena indeks bias dipengaruhi oleh suhu, penting untuk melakukan koreksi suhu jika alat tidak memiliki kompensasi suhu otomatis. Rumus koreksi suhu sederhana:



# Pengertian Uji Brix
if st.checkbox("Tampilkan Pengertian Uji Brix"):
    st.subheader("Apa itu Uji Brix?")
    st.write("""
    Uji Brix adalah metode pengukuran untuk menentukan kadar zat terlarut, terutama gula, dalam suatu larutan menggunakan refraktometer. 
    
    dalam 100 gram larutan.
    """)
    
    st.subheader("Rumus dan Koreksi Suhu")
    st.write("""
    Rumus perhitungan kadar Brix dengan koreksi suhu adalah:
    
    ```
    Brix Terkoreksi = Brix Awal + (Suhu - Suhu Referensi)*Koreksi per Derajat
    ```
    
    Di mana:
    - Suhu Referensi biasanya adalah 20°C.
    - Koreksi per Derajat adalah nilai koreksi yang berbeda tergantung pada refraktometer, umum digunakan 0.03°Bx/°C.
    """)

    st.subheader("Alat-Alat yang Digunakan")
    st.write("""
    Alat yang biasanya digunakan untuk uji Brix meliputi:
    - **Refraktometer**: Alat untuk mengukur indeks bias larutan.
    - **Thermometer**: Untuk mengukur suhu larutan.
    - **Pipet atau Dropper**: Untuk mengambil sampel larutan.
    """)

    st.subheader("Cara Melakukan Uji Brix")
    st.write("""
    1. Ambil sampel larutan menggunakan pipet.
    2. Letakkan sampel pada prisma refraktometer.
    3. Tutup prisma dan arahkan ke sumber cahaya.
    4. Baca nilai Brix yang ditunjukkan oleh refraktometer.
    5. Ukur suhu larutan dan lakukan koreksi jika suhu tidak sesuai dengan suhu referensi.
    """)

st.markdown("---")

if st.button("Hitung Koreksi Brix"):
    # Koreksi suhu sederhana: setiap kenaikan 1°C di atas 20°C, nilai brix bertambah 0.03°
    # (Catatan: ini nilai koreksi umum dan dapat disesuaikan berdasarkan alat)
    suhu_referensi = 20.0
    koreksi_per_derajat = 0.03

    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * koreksi_per_derajat
    brix_terkoreksi = brix_awal + koreksi

    st.success(f"Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")

    # Penilaian kualitas bahan pangan (contoh kategori)
    if brix_terkoreksi < 10:
        kualitas = "Rendah (contoh: buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar industri untuk buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, atau buah sangat manis)"

    st.info(f"Kategori Kadar Gula: {kualitas}")

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")
