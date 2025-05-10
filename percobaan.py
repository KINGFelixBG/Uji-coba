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

    # Pilihan Jenis Sampel
    sample_type = st.selectbox("Pilih jenis sampel yang diuji:", ["Jus Buah", "Sirup Gula", "Madu", "Air"])

    # Menentukan konstanta empiris (K) berdasarkan jenis sampel
    if sample_type == "Jus Buah":
        constant_K = 1.35  # Konstanta empiris untuk jus buah (perkiraan)
    elif sample_type == "Sirup Gula":
        constant_K = 1.50  # Konstanta empiris untuk sirup gula (perkiraan)
    elif sample_type == "Madu":
        constant_K = 1.58  # Konstanta empiris untuk madu (perkiraan)
    else:  # Air
        constant_K = 1.33  # Konstanta empiris untuk air (perkiraan)

    st.write(f"Konstanta empiris (K) untuk {sample_type} adalah: {constant_K}")

    # Input dari pengguna untuk indeks refraksi (n)
    refractive_index = st.number_input("Masukkan nilai indeks refraksi (n) dari refraktometer:", min_value=1.0, step=0.0001)

    # Kalkulasi Brix
    if st.button("Hitung Brix"):
        if refractive_index > 1.0 and constant_K > 0:
            brix = calculate_brix(refractive_index, constant_K)
            
            # Validasi jika hasil Brix lebih tinggi dari nilai wajar
            if brix > 80:
                st.error(f"Hasil Brix ({brix:.2f}%) terlalu tinggi. Mungkin ada kesalahan dalam pengukuran atau penggunaan konstanta.")
            elif brix > 70:
                st.warning(f"Hasil Brix ({brix:.2f}%) sangat tinggi. Pastikan cairan yang diuji sesuai dengan standar Brix.")
            elif brix > 60:
                st.warning(f"Hasil Brix ({brix:.2f}%) sangat tinggi. Periksa kembali cairan atau alat pengukur.")
            elif brix < 0:
                st.error("Hasil Brix negatif, kemungkinan ada kesalahan dalam pengukuran refraktometer.")
            else:
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

                # Penjelasan Sampel
                st.subheader("Penjelasan Sampel:")
                st.write("""
                ### Jenis Sampel
                - **Jus Buah**: Brix untuk jus buah umumnya berkisar antara 10% hingga 20%. Ini tergantung pada jenis buahnya, misalnya jus jeruk akan memiliki Brix yang lebih rendah dibandingkan dengan jus mangga.
                - **Sirup Gula**: Nilai Brix dapat mencapai hingga 60% atau lebih. Sirup gula yang sangat kental biasanya memiliki nilai Brix tinggi.
                - **Madu**: Madu memiliki nilai Brix yang tinggi, sekitar 80%, karena kandungan gula alami yang sangat tinggi.
                - **Air**: Air biasanya tidak mengandung gula, sehingga nilai Brix-nya adalah 0%.

                ### Pengambilan Sampel
                - Pastikan cairan yang diambil adalah sampel yang homogen dan representatif dari seluruh volume cairan. Jika cairan berwarna atau berbusa, pastikan untuk mencampurnya terlebih dahulu.
                - Gunakan alat yang bersih dan bebas dari kontaminasi. Pencampuran yang tidak tepat dapat mengubah konsentrasi gula dan menyebabkan pembacaan refraktometer yang tidak akurat.

                ### Pengaruh Suhu pada Sampel
                - Suhu cairan dapat memengaruhi pembacaan Brix. Sebaiknya pastikan cairan berada pada suhu kamar untuk hasil yang akurat, atau pastikan refraktometer sudah mengoreksi suhu secara otomatis.
                - Jika refraktometer tidak mengoreksi suhu otomatis, periksa suhu cairan dengan termometer dan lakukan koreksi sesuai instruksi refraktometer.

                ### Kesalahan Umum dalam Pengambilan Sampel
                - Pengambilan sampel yang tidak homogen atau pengukuran refraktometer yang tidak benar bisa mengarah pada kesalahan pembacaan. Oleh karena itu, pastikan untuk mengikuti prosedur yang tepat agar hasil yang didapat akurat dan sesuai.
                """)
        else:
            st.warning("Mohon masukkan nilai yang valid untuk indeks refraksi dan konstanta empiris.")
