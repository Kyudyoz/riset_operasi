import tkinter as tk
from tkinter import Button
import subprocess


# Fungsi untuk membuka aplikasi grafik
def open_grafik():
    window.withdraw()  # Menyembunyikan jendela utama
    subprocess.call(
        ["python", "grafik.py"]
    )  # Memanggil aplikasi grafik dengan proses subprocess
    window.deiconify()  # Mengembalikan jendela utama setelah aplikasi grafik ditutup


# Fungsi untuk membuka aplikasi simpleks
def open_simpleks():
    window.withdraw()  # Menyembunyikan jendela utama
    subprocess.call(
        ["python", "simplex.py"]
    )  # Memanggil aplikasi simpleks dengan proses subprocess
    window.deiconify()  # Mengembalikan jendela utama setelah aplikasi simpleks ditutup


# Fungsi untuk membuka aplikasi aljabar
def open_aljabar():
    window.withdraw()  # Menyembunyikan jendela utama
    subprocess.call(
        ["python", "aljabar.py"]
    )  # Memanggil aplikasi aljabar dengan proses subprocess
    window.deiconify()  # Mengembalikan jendela utama setelah aplikasi aljabar ditutup


window = tk.Tk()
window.title("Pilihan Aplikasi")

grafik_button = Button(
    window, text="Grafik", command=open_grafik
)  # Tombol untuk membuka aplikasi grafik
grafik_button.pack()

simpleks_button = Button(
    window, text="Simpleks", command=open_simpleks
)  # Tombol untuk membuka aplikasi simpleks
simpleks_button.pack()

aljabar_button = Button(
    window, text="Aljabar", command=open_aljabar
)  # Tombol untuk membuka aplikasi aljabar
aljabar_button.pack()

window.mainloop()
