import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def process_text():
    shift_value = shift_entry.get()
    input_text = input_text_box.get("1.0", "end-1c")
    try:
        shift = int(shift_value)
        if encrypt_var.get() == 1:
            output = enkripsi(input_text, shift)
        else:
            output = deskripsi(input_text, shift)
        output_text_box.config(state='normal')
        output_text_box.delete("1.0", "end")
        output_text_box.insert("1.0", output)
        output_text_box.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid.")

# Membuat window
window = tk.Tk()
window.title("Cipher Encryption Machine")
window.configure(bg="#ffe4e1", padx=0, pady=0)

# Frame kotak abu-abu untuk judul
title_frame = tk.Frame(window, bg="#cccccc", padx=10, pady=10)
title_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Label judul utama
title_label = tk.Label(title_frame, text="CIPHER ENCRYPTION MACHINE", font=("Arial", 25, "bold"), bg="#cccccc")
title_label.pack(fill="x", pady=10)

# Atur agar title_frame memenuhi seluruh lebar dari sisi kiri ke kanan
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=0)

# Spasi antara judul dan "Set Shift Value"
title_frame.grid(pady=(0, 20))

# Style untuk ttk
style = ttk.Style()
style.configure("TLabel", background="#ffe4e1", foreground="#333333", font=("Arial", 16, "bold"))
style.configure("TButton", background="#f8a5c2", font=("Arial", 16, "bold"))
style.configure("TRadiobutton", font=("Arial", 16, "bold"))

# Label dan Entry untuk Shift
shift_label = ttk.Label(window, text="Set Shift Value :")
shift_label.grid(row=1, column=0, columnspan=3, pady=(20, 10), padx=(30, 0))  # Mengatur padding agar label bergeser ke kiri
shift_label.config(font=("Arial", 20, "bold"))
shift_entry = ttk.Entry(window, width=5)
shift_entry.grid(row=2, column=0, columnspan=3, pady=(0, 20), padx=(30, 0))  # Mengatur padding agar entry bergeser ke kiri
shift_entry.config(font=("Arial", 20, "bold"))

# Text Box untuk Input
input_label = ttk.Label(window, text="Input Text to Encrypt/Decrypt")
input_label.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=200, pady=(20, 0))
input_label.config(font=("Arial", 20, "bold"))
input_text_box = tk.Text(window, height=50, width=50, font=("Arial", 20))  # Mengurangi tinggi dan lebar TextBox
input_text_box.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=200, pady=(0, 30))

# Mengatur Frame untuk tombol radio dan tombol proses
radio_frame = tk.Frame(window, bg="#ffe4e1")
radio_frame.grid(row=5, column=0, columnspan=3, pady=(0, 10), sticky="nsew")

# Frame untuk pilihan Encrypt dan Decrypt
radio_frame = ttk.Frame(window)
radio_frame.grid(row=5, column=0, columnspan=3, pady=(10, 20))

# Pilihan Encrypt atau Decrypt
encrypt_var = tk.IntVar()
encrypt_var.set(1)  # Default to Encrypt
encrypt_radio = ttk.Radiobutton(radio_frame, text="ENCRYPT", variable=encrypt_var, value=1)
decrypt_radio = ttk.Radiobutton(radio_frame, text="DECRYPT", variable=encrypt_var, value=0)
encrypt_radio.grid(row=0, column=0, padx=10)  # Mengatur padding agar radio button bergeser sedikit
decrypt_radio.grid(row=0, column=1, padx=10)

# Atur kolom di radio_frame agar berada di tengah
radio_frame.grid_columnconfigure(0, weight=1)
radio_frame.grid_columnconfigure(1, weight=1)

# Tombol untuk Memproses
process_button = ttk.Button(radio_frame, text="PROCESS TEXT", command=process_text)
process_button.grid(row=0, column=2, padx=(10, 20))  # Mengatur padding agar tombol bergeser ke kiri

# Text Box untuk Output
output_label = ttk.Label(window, text="Output")
output_label.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=200, pady=(20, 0))
output_label.config(font=("Arial", 20, "bold"))
output_text_box = tk.Text(window, height=50, width=50, font=("Arial", 20), state='disabled')  # Mengurangi tinggi dan lebar TextBox
output_text_box.grid(row=7, column=0, columnspan=3, sticky="nsew", padx=200, pady=(0, 50))

# Mengatur baris dan kolom agar responsif
window.rowconfigure(4, weight=1)
window.rowconfigure(7, weight=1)

# Jalankan window
window.mainloop()