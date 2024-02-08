import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ffmpeg
import threading

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

app = tk.Tk()
app.title("Convertidor de Video")

btn_seleccionar = tk.Button(app, text="Seleccionar Video", command=seleccionar_archivos)
btn_seleccionar.pack(pady=20)

app.mainloop()
