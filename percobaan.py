import streamlit as st


# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Bahasa
bahasa = st.sidebar.selectbox("Pilih Bahasa / Select Language", ["Indonesia", "English"])

# Fungsi teks multi bahasa
def _(indo, eng):
    return indo if bahasa == "Indonesia" else eng

st.title(_("Uji Brix pada Bahan Pangan", "Brix Test on Food Ingredients"))

st.write(_(
    "Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu.",
    "This app helps calculate the Brix level of sugar solution in food ingredients, with temperature correction."
))

# Sidebar untuk input
with st.sidebar:
    st.header(_("Input Parameter", "Input Parameters"))
    brix_awal = st.slider(_("Nilai Brix dari refraktometer (°Bx)", "Brix value from refractometer (°Bx)"), 0.0, 85.0, 10.0, 0.1)
    suhu = st.slider(_("Suhu larutan saat pengukuran (°C)", "Solution temperature at measurement (°C)"), 0.0, 100.0, 25.0, 0.1)
    show_dark_mode = st.checkbox("🌙 " + _("Mode Gelap", "Dark Mode"))
    uploaded_image = st.file_uploader(_("Upload gambar sampel", "Upload sample image"), type=['jpg', 'png'])

# Dark mode otomatis
if show_dark_mode or datetime.now().hour >= 18:
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Simulasi koreksi dan visualisasi
suhu_referensi = 20.0
faktor_koreksi = 0.03
selisih_suhu = suhu - suhu_referensi
koreksi = selisih_suhu * faktor_koreksi
brix_terkoreksi = brix_awal + koreksi

# Tampilkan hasil
st.metric(_("Nilai Brix Terkoreksi", "Corrected Brix Value"), f"{brix_terkoreksi:.2f} °Bx")

# Penilaian kualitas
if brix_terkoreksi < 10:
    kualitas = _("Rendah (buah belum matang)", "Low (unripe fruit)")
elif 10 <= brix_terkoreksi <= 15:
    kualitas = _("Sedang (standar industri)", "Medium (industry standard)")
else:
    kualitas = _("Tinggi (madu, sirup)", "High (honey, syrup)")

st.info(_("Kategori Gula: ", "Sugar Level: ") + kualitas)

# Upload gambar hasil uji
if uploaded_image:
    st.image(uploaded_image, caption=_("Gambar sampel", "Sample image"), use_column_width=True)

# Grafik suhu vs koreksi
if st.checkbox(_("Tampilkan Grafik", "Show Chart")):
    temps = list(range(0, 101))
    koreksi_list = [(t - suhu_referensi) * faktor_koreksi for t in temps]
    hasil_koreksi = [brix_awal + k for k in koreksi_list]
    fig, ax = plt.subplots()
    ax.plot(temps, hasil_koreksi, label="Brix Terkoreksi")
    ax.axvline(suhu, color='r', linestyle='--', label="Suhu Anda")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Nilai Brix")
    ax.set_title("Visualisasi Koreksi Brix")
    ax.legend()
    st.pyplot(fig)

# Penjelasan Brix
with st.expander("📘 " + _("Apa itu Uji Brix?", "What is Brix Test?")):
    st.markdown(_(
        """
        **Derajat Brix (°Bx)** menunjukkan jumlah zat padat terlarut, terutama gula, dalam 100 gram larutan.
        Koreksi suhu penting jika alat tidak otomatis menyesuaikan.
        """,
        """
        **Degrees Brix (°Bx)** indicate the amount of dissolved solids, mainly sugar, in 100 grams of solution.
        Temperature correction is essential if your tool lacks automatic compensation.
        """
    ))

# Unduh hasil sebagai PDF
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hasil Uji Brix", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Brix Awal: {brix_awal} °Bx", ln=2)
    pdf.cell(200, 10, txt=f"Suhu: {suhu} °C", ln=3)
    pdf.cell(200, 10, txt=f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx", ln=4)
    pdf.cell(200, 10, txt=f"Kategori: {kualitas}", ln=5)
    buffer = BytesIO()
    pdf.output(buffer)
    return buffer

if st.button(_("Unduh Hasil PDF", "Download PDF Report")):
    pdf_file = create_pdf()
    st.download_button(label="📄 Unduh PDF", data=pdf_file, file_name="hasil_uji_brix.pdf")

# Riwayat uji
if 'history' not in st.session_state:
    st.session_state.history = []

st.session_state.history.append({"brix": brix_awal, "suhu": suhu, "hasil": brix_terkoreksi})

with st.expander("📊 " + _("Riwayat Uji", "Test History")):
    st.table(pd.DataFrame(st.session_state.history))

st.caption("📘 " + _("Dibuat untuk edukasi uji Brix", "Created for Brix test education"))
