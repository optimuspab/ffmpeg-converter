import tkinter as tk
from tkinter import filedialog
import ffmpeg

def convertir_video(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file)
        .run()
    )

def seleccionar_archivo():
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        output_file_path = input_file_path.split('.')[0] + '_convertido.mp4'
        convertir_video(input_file_path, output_file_path)
        tk.messagebox.showinfo("Convertido", "El video ha sido convertido con éxito.")

app = tk.Tk()
app.title("Convertidor de Video")

btn_seleccionar = tk.Button(app, text="Seleccionar Video", command=seleccionar_archivo)
btn_seleccionar.pack(pady=20)

app.mainloop()
