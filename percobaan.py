import streamlit as st

# Function to calculate Brix based on the refractive index and constant
def calculate_brix(n, K):
    # Applying the formula Brix = (100 * (n - 1)) / K
    brix = (100 * (n - 1)) / K
    return brix

# Streamlit App
st.title("Kalkulator Uji Brix")

# Opsi Menu
menu = ["Uji Brix", "Kalkulator Uji Brix"]
choice = st.sidebar.selectbox("Pilih Opsi:", menu)

# Opsi "Uji Brix"
if choice == "Uji Brix":
    st.header("Pengertian Uji Brix")
    st.write("""
    Uji Brix adalah pengujian yang digunakan untuk mengukur kandungan gula dalam larutan, khususnya dalam cairan seperti jus buah, madu, atau sirup.
    Pengukuran ini dilakukan menggunakan alat yang disebut **refraktometer**, yang mengukur pembiasan cahaya yang terjadi ketika cahaya melewati cairan yang diuji.

    ### Rumus Uji Brix
    Rumus perhitungan Brix yang lebih detail berdasarkan pengukuran indeks refraksi adalah:
    - **Brix = (100 × (n - 1)) / K**
    - Di mana `n` adalah indeks refraksi dan `K` adalah konstanta empiris yang dapat bervariasi tergantung pada suhu dan komposisi larutan.

    ### Alat yang Digunakan
    - **Refractometer Handheld**: Alat utama yang digunakan untuk mengukur pembiasan cahaya dalam cairan.
    - **Termometer** (jika diperlukan): Beberapa refraktometer memerlukan penyesuaian suhu agar perhitungan Brix lebih akurat.

    ### Cara Menggunakan Alat
    1. Ambil sedikit sampel cairan yang akan diuji.
    2. Letakkan cairan di atas prisma refraktometer.
    3. Tutup tutup refraktometer dan arahkan ke cahaya.
    4. Lihat pembacaan Brix yang muncul pada skala refraktometer.
    5. Catat hasil pembacaan tersebut.

    Penggunaan refraktometer dengan cara yang benar akan memberikan hasil yang akurat untuk menentukan kandungan gula dalam cairan tersebut.
    """)

# Opsi "Kalkulator Uji Brix"
if choice == "Kalkulator Uji Brix":
    st.header("Kalkulator Uji Brix")

    # Input dari pengguna
    refractive_index = st.number_input("Masukkan nilai indeks refraksi (n) dari refraktometer:", min_value=1.0, step=0.0001)
    constant_K = st.number_input("Masukkan konstanta empiris (K) yang sesuai untuk larutan:", min_value=1.0, step=0.01)

    # Kalkulasi Brix
    if st.button("Hitung Brix"):
        if refractive_index > 1.0 and constant_K > 0:
            brix = calculate_brix(refractive_index, constant_K)
            st.write(f"Brix yang dihitung adalah: {brix:.2f} %")

            # Penjelasan cara penyelesaian dan alasan
            st.subheader("Cara Penyelesaian:")
            st.write(f"1. Pembacaan refraktometer menghasilkan nilai indeks refraksi: {refractive_index}.")
            st.write(f"2. Konstanta empiris yang digunakan untuk cairan ini adalah {constant_K}.")
            st.write(f"3. Menggunakan rumus Brix = (100 × (n - 1)) / K.")
            st.write(f"4. Dengan memasukkan nilai-nilai tersebut, kita menghitung Brix: {brix:.2f} %.")

            # Penjelasan alasan dan keterangan
            st.subheader("Alasan dan Keterangan:")
            st.write("""
            - **Brix** adalah pengukuran yang digunakan untuk menentukan persentase total padatan terlarut dalam cairan, terutama untuk kandungan gula.
            - Menggunakan rumus di atas, kita dapat menghitung nilai Brix dengan mengukur indeks refraksi cairan dan memasukkan konstanta empiris yang sesuai.
            - Pembacaan yang tepat pada refraktometer sangat penting untuk mendapatkan hasil yang akurat. Jika cairan terlalu panas atau terlalu dingin, koreksi suhu mungkin diperlukan.
            """)
        else:
            st.warning("Mohon masukkan nilai yang valid untuk indeks refraksi dan konstanta empiris.")
