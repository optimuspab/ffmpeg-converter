import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import threading

def convertir_video(input_file, output_file, progress_var):
    (
        ffmpeg
        .input(input_file)
        .output(output_file)
        .run(cmd=update_progress, progress_var=progress_var)
    )

def update_progress(progress, progress_var):
    progress_var.set(progress)

def procesar_archivos(files, progress_var):
    total_files = len(files)
    for idx, input_file in enumerate(files, start=1):
        output_file = input_file.split('.')[0] + '_convertido.mp4'
        convertir_video(input_file, output_file, progress_var)
        progress = (idx / total_files) * 100
        update_progress(progress, progress_var)
    messagebox.showinfo("Convertido", "Todos los videos han sido convertidos con éxito.")

def seleccionar_archivos():
    input_files = filedialog.askopenfilenames()
    if input_files:
        progress_var = tk.DoubleVar()
        progress_var.set(0)
        progress_window = tk.Toplevel()
        progress_window.title("Progreso de la conversión")
        progress_bar = tk.Progressbar(progress_window, variable=progress_var, maximum=100)
        progress_bar.pack(padx=20, pady=10)
        threading.Thread(target=procesar_archivos, args=(list(input_files), progress_var)).start()

app = tk.Tk()
app.title("ffmpeg Video Converter")

btn_seleccionar = tk.Button(app, text="Seleccionar Videos", command=seleccionar_archivos)
btn_seleccionar.pack(pady=20)

app.mainloop()
