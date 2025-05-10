import streamlit as st

# Function to calculate Brix
def calculate_brix(reading, refractometer_constant):
    brix = reading * refractometer_constant
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
    Rumus perhitungan Brix adalah:
    - **Brix = (Panjang gelombang cahaya yang dibiaskan) x Konstanta refraktometer**
    - Pada dasarnya, Brix mengindikasikan persen berat padatan terlarut dalam cairan tersebut (terutama gula).

    ### Alat yang Digunakan
    - **Refractometer Handheld**: Alat utama yang digunakan untuk mengukur pembiasan cahaya dalam cairan. 
    - **Termometer** (jika diperlukan): Beberapa refraktometer memerlukan penyesuaian suhu.

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
    reading = st.number_input("Masukkan pembacaan refraktometer (nilai Brix):", min_value=0.0, step=0.1)
    refractometer_constant = st.number_input("Masukkan konstanta refraktometer:", min_value=1.0, step=0.01)

    # Kalkulasi Brix
    if st.button("Hitung Brix"):
        if reading > 0 and refractometer_constant > 0:
            brix = calculate_brix(reading, refractometer_constant)
            st.write(f"Brix yang dihitung adalah: {brix:.2f}")

            # Penjelasan cara penyelesaian dan alasan
            st.subheader("Cara Penyelesaian:")
            st.write(f"1. Pembacaan refraktometer adalah {reading}.")
            st.write(f"2. Konstanta refraktometer yang digunakan adalah {refractometer_constant}.")
            st.write(f"3. Menggunakan rumus Brix = (Pembacaan refraktometer) x Konstanta refraktometer.")
            st.write(f"4. Brix yang dihitung adalah: {brix:.2f}.")

            # Penjelasan alasan dan keterangan
            st.subheader("Alasan dan Keterangan:")
            st.write("""
            - **Brix** adalah pengukuran yang digunakan untuk menentukan persentase total padatan terlarut dalam cairan, terutama untuk kandungan gula.
            - Hasil pengukuran ini sangat berguna dalam industri makanan dan minuman, terutama untuk mengontrol kualitas produk dan memastikan konsistensi rasa.
            - Pembacaan yang tepat pada refraktometer sangat penting untuk mendapatkan hasil yang akurat. Kesalahan dalam pengambilan sampel atau suhu cairan dapat memengaruhi hasil perhitungan.
            """)
        else:
            st.warning("Mohon masukkan nilai yang valid untuk pembacaan dan konstanta refraktometer.")
