import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ffmpeg
import threading
import os

def convertir_video(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file)
        .run()
    )

def procesar_archivos(files):
    for input_file in files:
        output_file = input_file.split('.')[0] + '_convertido.mp4'
        convertir_video(input_file, output_file)
    messagebox.showinfo("Convertido", "Todos los videos han sido convertidos con éxito.")

def seleccionar_archivos():
    input_files = filedialog.askopenfilenames()
    if input_files:
        files_to_process = list(input_files)
        threading.Thread(target=procesar_archivos, args=(files_to_process,)).start()
        actualizar_archivos_seleccionados(input_files)

def actualizar_archivos_seleccionados(files):
    archivos_seleccionados_texto.config(state=tk.NORMAL)
    archivos_seleccionados_texto.delete('1.0', tk.END)
    for file_path in files:
        file_name = os.path.basename(file_path)
        archivos_seleccionados_texto.insert(tk.END, file_name + '\n')
    archivos_seleccionados_texto.config(state=tk.DISABLED)


app = tk.Tk()
app.title("ffmpeg video Converter")
app.geometry("300x400")
app.resizable(True, True)
#app.config(bg='#457B9D')

label = tk.Label(app, font=('Segoe UI', 15, 'bold'), fg='#212529', wraplength=200, text="Selecciona el video o videos a convertir con ffmpeg\n")
label.pack(pady=20)

btn_seleccionar = tk.Button(app, bg='#212529', fg='#F1FAEE', text="Seleccionar Video", command=seleccionar_archivos)
btn_seleccionar.pack(pady=20)

archivos_seleccionados_label = tk.Label(app, bg='#212529', fg='#F1FAEE', text="Archivos Seleccionados:")
archivos_seleccionados_label.pack(pady=(0, 10))

archivos_seleccionados_texto = tk.Text(app, bg='#F8F9FA', height=6, width=35)
archivos_seleccionados_texto.pack()

app.mainloop()
