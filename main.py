import tkinter as tk
from tkinter import Button
import subprocess

def open_grafik():
    window.withdraw() 
    subprocess.call(["python", "grafik.py"])
    window.deiconify()  

def open_simpleks():
    window.withdraw()
    subprocess.call(["python", "simplex.py"])
    window.deiconify()

def open_aljabar():
    window.withdraw()
    subprocess.call(["python", "aljabar.py"])
    window.deiconify()

window = tk.Tk()
window.title("Pilihan Aplikasi")

grafik_button = Button(window, text="Grafik", command=open_grafik)
grafik_button.pack()

simpleks_button = Button(window, text="Simpleks", command=open_simpleks)
simpleks_button.pack()

aljabar_button = Button(window, text="Aljabar", command=open_aljabar)
aljabar_button.pack()

window.mainloop()
