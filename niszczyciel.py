# made by kabolek
# easy to edit. feel free to edit

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Label, Toplevel

def destroy_files():
    file_paths = filedialog.askopenfilenames(title="Wybierz pliki do zniszczenia")
    if not file_paths:
        return
    
    deleted_files = []
    failed_files = []
    log_data = []
    
    for file_path in file_paths:
        try:
            file_size = os.path.getsize(file_path)  # Pobranie rozmiaru pliku
            file_extension = os.path.splitext(file_path)[1]  # Pobranie rozszerzenia pliku
            os.remove(file_path)
            deleted_files.append(file_path)
            log_data.append(f"Plik: {os.path.basename(file_path)}, Rozmiar: {file_size}B, Rozszerzenie: {file_extension}")
        except Exception as e:
            failed_files.append(file_path)
    
    export_log(log_data)
    show_destruction_message(len(deleted_files), len(failed_files))

def export_log(log_data):
    if log_data:
        log_file = "usunięte_pliki.txt"
        with open(log_file, 'w') as f:
            for line in log_data:
                f.write(line + "\n")
        messagebox.showinfo("Log zapisany", f"Zapisano log usuniętych plików w {log_file}")

def show_destruction_message(success_count, fail_count):
    message_window = Toplevel(root)
    message_window.title("Pliki zniszczone")
    message_window.geometry("300x150")
    
    message = f"Usunięto {success_count} plików!"
    if fail_count > 0:
        message += f"\nNie udało się usunąć {fail_count} plików."
    
    text_label = Label(message_window, text=message, font=("Arial", 14, "bold"), fg="red")
    text_label.pack(pady=20)
    
    messagebox.showinfo("Sukces", message)

root = tk.Tk()
root.title("Niszczyciel plików")
root.geometry("400x200")

destroy_button = tk.Button(root, text="Wybierz pliki do zniszczenia", command=destroy_files, font=("Arial", 14), bg="red", fg="white")
destroy_button.pack(pady=20)

root.mainloop()
