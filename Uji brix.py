import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

def hitung_molaritas():
    try:
        mol = float(entry_mol.get())
        volume = float(entry_volume.get())
        hasil = mol / volume
        langkah = (
            f"Langkah-langkah:\n"
            f"1. Diketahui jumlah mol = {mol} mol, volume larutan = {volume} L.\n"
            f"2. Gunakan rumus: Molaritas = mol / volume.\n"
            f"3. Molaritas = {mol} / {volume} = {hasil:.4f} M.\n"
        )
        messagebox.showinfo("Hasil", f"Molaritas = {hasil:.4f} M\n\n{langkah}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

def hitung_brix():
    try:
        massa_larutan = float(entry_massa_larutan.get())
        massa_zat_terlarut = float(entry_massa_zat_terlarut.get())
        hasil = (massa_zat_terlarut / massa_larutan) * 100
        langkah = (
            f"Langkah-langkah:\n"
            f"1. Diketahui massa larutan = {massa_larutan} gram, massa zat terlarut = {massa_zat_terlarut} gram.\n"
            f"2. Gunakan rumus: Brix = (massa zat terlarut / massa larutan) * 100.\n"
            f"3. Brix = ({massa_zat_terlarut} / {massa_larutan}) * 100 = {hasil:.2f}%.\n"
        )
        messagebox.showinfo("Hasil", f"Brix = {hasil:.2f}%\n\n{langkah}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

def show_info():
    info_window = Toplevel(root)
    info_window.title("Informasi dan Rumus")
    tk.Label(info_window, text="Pengertian, Rumus, dan Alat-Alat", font=("Arial", 16, "bold")).pack(pady=10)

    text = (
        "1. Molaritas (M): Jumlah mol zat terlarut per liter larutan.\n"
        "   Rumus: M = mol / volume (L)\n"
        "   Alat: Gelas ukur, timbangan.\n\n"
        "2. Normalitas (N): Jumlah ekuivalen zat terlarut per liter larutan.\n"
        "   Rumus: N = (mol * valensi) / volume (L)\n"
        "   Alat: Gelas ukur, timbangan.\n\n"
        "3. Molalitas (m): Jumlah mol zat terlarut per kilogram pelarut.\n"
        "   Rumus: m = mol / massa pelarut (kg)\n"
        "   Alat: Timbangan.\n\n"
        "4. Brix (%): Konsentrasi gula dalam larutan.\n"
        "   Rumus: Brix = (massa zat terlarut / massa larutan) * 100\n"
        "   Alat: Timbangan, refraktometer.\n\n"
    )
    tk.Label(info_window, text=text, justify="left").pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Kalkulator Konsentrasi Kimia")

# Label dan Entry untuk input
tk.Label(root, text="Jumlah Mol (mol):").grid(row=0, column=0)
entry_mol = tk.Entry(root)
entry_mol.grid(row=0, column=1)

tk.Label(root, text="Volume Larutan (L):").grid(row=1, column=0)
entry_volume = tk.Entry(root)
entry_volume.grid(row=1, column=1)

tk.Label(root, text="Massa Larutan (gram):").grid(row=2, column=0)
entry_massa_larutan = tk.Entry(root)
entry_massa_larutan.grid(row=2, column=1)

tk.Label(root, text="Massa Zat Terlarut (gram):").grid(row=3, column=0)
entry_massa_zat_terlarut = tk.Entry(root)
entry_massa_zat_terlarut.grid(row=3, column=1)

# Tombol untuk perhitungan
tk.Button(root, text="Hitung Molaritas", command=hitung_molaritas).grid(row=4, column=0, pady=5)
tk.Button(root, text="Hitung Brix", command=hitung_brix).grid(row=4, column=1, pady=5)

# Tombol untuk informasi
tk.Button(root, text="Pengertian & Rumus", command=show_info).grid(row=5, column=0, pady=5, columnspan=2)

root.mainloop()
