import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Crypto.Cipher import DES
import base64

# Fungsi padding dan enkripsi DES
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

def process_text():
    plain_text = input_text_box.get("1.0", "end-1c")
    key_input = key_entry.get()

    if len(key_input) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang tepat 8 karakter.")
        return

    key = key_input.encode('utf-8')

    try:
        if encrypt_var.get() == 1:
            output = encrypt(plain_text, key)
        else:
            output = decrypt(plain_text, key)
        output_text_box.config(state='normal')
        output_text_box.delete("1.0", "end")
        output_text_box.insert("1.0", output)
        output_text_box.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat window
window = tk.Tk()
window.title("DES Encryption/Decryption Machine")
window.configure(bg="#E0F7FA")
window.state("zoomed")  # Membuat tampilan fullscreen

# Konfigurasi grid agar responsif
for i in range(10):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

# Frame untuk judul yang memenuhi kiri, kanan, dan atas
title_frame = tk.Frame(window, bg="#80DEEA")
title_frame.grid(row=0, column=0, columnspan=10, sticky="nsew")  # Sticky untuk kiri, kanan, atas

title_label = tk.Label(title_frame, text="DES ENCRYPTION/DECRYPTION MACHINE", 
                       font=("Arial", 30, "bold"), bg="#80DEEA")
title_label.pack(pady=10)


# Input untuk Key
key_label = ttk.Label(window, text="Set Key (8 characters):", font=("Arial", 18), background="#E0F7FA")
key_label.grid(row=1, column=1, columnspan=8, sticky="n", pady=(10, 5))
key_entry = ttk.Entry(window, font=("Arial", 16), width=20, justify="center")
key_entry.grid(row=2, column=1, columnspan=8, sticky="n", pady=(0, 20))

# Input Text
input_label = ttk.Label(window, text="Input Text to Encrypt/Decrypt:", font=("Arial", 18), background="#E0F7FA")
input_label.grid(row=3, column=1, columnspan=8, sticky="n", pady=(10, 5))
input_text_box = tk.Text(window, font=("Arial", 16), height=5, width=50)
input_text_box.grid(row=4, column=1, columnspan=8, sticky="nsew", padx=20)

# Radio Buttons dan Tombol Proses
radio_frame = ttk.Frame(window)
radio_frame.grid(row=5, column=1, columnspan=8, pady=10)
encrypt_var = tk.IntVar(value=1)
encrypt_radio = ttk.Radiobutton(radio_frame, text="ENCRYPT", variable=encrypt_var, value=1)
decrypt_radio = ttk.Radiobutton(radio_frame, text="DECRYPT", variable=encrypt_var, value=0)
process_button = ttk.Button(radio_frame, text="PROCESS TEXT", command=process_text)
encrypt_radio.grid(row=0, column=0, padx=10)
decrypt_radio.grid(row=0, column=1, padx=10)
process_button.grid(row=0, column=2, padx=10)

# Output Text
output_label = ttk.Label(window, text="Output:", font=("Arial", 18), background="#E0F7FA")
output_label.grid(row=6, column=1, columnspan=8, sticky="n", pady=(10, 5))
output_text_box = tk.Text(window, font=("Arial", 16), height=5, width=50, state="disabled")
output_text_box.grid(row=7, column=1, columnspan=8, sticky="nsew", padx=20, pady=(0, 20))

# Jalankan window
window.mainloop()
