import tkinter as tk
from tkinter import filedialog
from stegano import lsb
import os

# Fungsi tetap sama, hanya UI yang dimodifikasi
def browse_image():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
    if img_path:
        img_path_entry.delete(0, tk.END)
        img_path_entry.insert(0, img_path)

def browse_save_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if save_path:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, save_path)

def hide_message():
    img_path = img_path_entry.get().strip()
    message = message_entry.get().strip()
    save_path = save_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    if not message:
        result_label.config(text="Error: Pesan tidak boleh kosong.", fg="red")
        return

    if not save_path:
        result_label.config(text="Error: Path penyimpanan tidak valid.", fg="red")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        result_label.config(text=f"Pesan berhasil disembunyikan di: {save_path}", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

def show_message():
    img_path = img_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            result_label.config(text=f"Pesan tersembunyi: {clear_message}", fg="green")
        else:
            result_label.config(text="Tidak ada pesan tersembunyi dalam gambar.", fg="orange")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

# Warna tema hijau lembut
bg_color = "#F3E5F5"  # Soft lilac background
header_color = "#CE93D8"  # Light lilac header
button_color = "#AB47BC"  # Button lilac
frame_color = "#D1C4E9"  # Frame background lilac
text_color = "#424242"  # Dark text color

# Setup root window
root = tk.Tk()
root.title("Steganography Tool")
root.configure(bg=bg_color)
root.geometry("600x450")
root.resizable(True, True)

# Heading
header_label = tk.Label(root, text="Steganography Tool", font=("Arial", 18, "bold"), bg=header_color, fg="white", pady=10)
header_label.pack(fill="x")

# Input frame
input_frame = tk.LabelFrame(root, text="Input dan Pengaturan", font=("Arial", 12, "bold"), bg=frame_color, fg=text_color, padx=10, pady=10)
input_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Path gambar
tk.Label(input_frame, text="Path Gambar:", font=("Arial", 12), bg=frame_color, fg=text_color).grid(row=0, column=0, sticky="w", pady=5)
img_path_entry = tk.Entry(input_frame, font=("Arial", 12))
img_path_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
browse_img_button = tk.Button(input_frame, text="Browse", command=browse_image, bg=button_color, fg="white", font=("Arial", 10, "bold"))
browse_img_button.grid(row=0, column=2, padx=5)

# Pesan tersembunyi
tk.Label(input_frame, text="Pesan:", font=("Arial", 12), bg=frame_color, fg=text_color).grid(row=1, column=0, sticky="w", pady=5)
message_entry = tk.Entry(input_frame, font=("Arial", 12))
message_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=5, columnspan=2)

# Path penyimpanan
tk.Label(input_frame, text="Simpan ke:", font=("Arial", 12), bg=frame_color, fg=text_color).grid(row=2, column=0, sticky="w", pady=5)
save_path_entry = tk.Entry(input_frame, font=("Arial", 12))
save_path_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
browse_save_button = tk.Button(input_frame, text="Browse", command=browse_save_path, bg=button_color, fg="white", font=("Arial", 10, "bold"))
browse_save_button.grid(row=2, column=2, padx=5)

# Responsive configuration
input_frame.columnconfigure(1, weight=1)

# Radio button frame
radio_frame = tk.Frame(root, bg=bg_color)
radio_frame.pack(pady=5)
mode_var = tk.StringVar(value="hide")
tk.Radiobutton(radio_frame, text="Sembunyikan", variable=mode_var, value="hide", font=("Arial", 12), bg=bg_color, fg=text_color).pack(side="left", padx=10)
tk.Radiobutton(radio_frame, text="Tampilkan", variable=mode_var, value="reveal", font=("Arial", 12), bg=bg_color, fg=text_color).pack(side="left", padx=10)

# Action buttons
action_frame = tk.Frame(root, bg=bg_color)
action_frame.pack(pady=10)
hide_button = tk.Button(action_frame, text="Proses", command=lambda: hide_message() if mode_var.get() == "hide" else show_message(), 
                        bg=button_color, fg="white", font=("Arial", 12, "bold"), width=20)
hide_button.pack()

# Output result
output_frame = tk.LabelFrame(root, text="Hasil", font=("Arial", 12, "bold"), bg=frame_color, fg=text_color, padx=10, pady=10)
output_frame.pack(fill="both", padx=20, pady=10)
result_label = tk.Label(output_frame, text="", font=("Arial", 12), bg=frame_color, fg=text_color, wraplength=500)
result_label.pack()

# Run the app
root.mainloop()