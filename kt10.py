import psutil
import subprocess
from tkinter import *

#def open_app():
    #subprocess.Popen(['python', 't103.py'], shell=True)

#def close_app():
    #subprocess.Popen(["TASKKILL", "/F", "/IM", "pythonw.exe", "/T"])

root = Tk()
root.geometry("450x350")

def close_app():
    for proc in psutil.process_iter():
        if "python" in proc.name():
            proc.terminate()

def open_app():
    open_button.config(state=DISABLED)
    subprocess.Popen(['python', 't103.py'], shell=True)

open_button = Button(root, text="Открыть", padx=25, pady=15, width=10,bd=5, font=('Arial', 15), bg="RED", command=open_app)
open_button.pack()

close_button = Button(root, text="Закрыть", padx=25, pady=15, width=10,
bd=5, font=('Arial', 15), bg="GREEN", command=close_app)
close_button.pack()

root.mainloop()