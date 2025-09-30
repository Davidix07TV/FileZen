import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    folder_path = folder_entry.get()
    if not folder_path or not os.path.exists(folder_path):
        messagebox.showerror("Errore", "Seleziona una cartella valida!")
        return

    # Scorri tutti i file nella cartella
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Controlla se il file ha estensione
            if '.' in file_name:
                ext = file_name.split('.')[-1].upper()
            else:
                ext = "NO_EXT"
            
            # Crea cartella per l'estensione se non esiste
            ext_folder = os.path.join(folder_path, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            # Sposta il file
            shutil.move(file_path, os.path.join(ext_folder, file_name))

    messagebox.showinfo("FileZen", "✅ Organizzazione completata!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

# ---------------- GUI -----------------
root = tk.Tk()
root.title("FileZen 🧘‍♂️ - Avanzato")
root.geometry("450x220")
root.configure(bg="#f0f4f8")

title_label = tk.Label(root, text="FileZen - Organizza tutti i tuoi file", font=("Helvetica", 16), bg="#f0f4f8")
title_label.pack(pady=10)

folder_entry = tk.Entry(root, width=45, font=("Helvetica", 12))
folder_entry.pack(pady=5, padx=10)

browse_button = tk.Button(root, text="Seleziona cartella", command=browse_folder, font=("Helvetica", 12), bg="#2196F3", fg="white")
browse_button.pack(pady=5)

organize_button = tk.Button(root, text="Organizza!", command=organize_files, font=("Helvetica", 14), bg="#4CAF50", fg="white")
organize_button.pack(pady=15)

root.mainloop()
