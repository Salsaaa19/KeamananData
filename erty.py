from stegano import lsb
import os

def get_image_path():
    """
    Meminta pengguna untuk memasukkan path gambar.
    Memverifikasi apakah file tersebut ada dan memiliki format yang sesuai.
    """
    while True:
        img_path = input("Masukkan path gambar seperti ini : (/Users/salsabilawidya/Documents/KAMPUS/Semester 5/Keamanan Data dan Informasi/Prak4/anya.jpg):" )
        if os.path.exists(img_path) and img_path.endswith(('.png','jpg')):
            return img_path
        else:
            print("Path gambar tidak valid atau format salah")

def hide_message():
    img_path = get_image_path() #Perbaikan : Fungsi dipanggil dengan kurung
    message = input("Masukkan pesan rahasia yang akan di sembunyikan : ")

    try:
        # Proses menyembunyikan pesan
        secret = lsb.hide(img_path, message)
        save_path = input("/Users/salsabilawidya/Documents/KAMPUS/Semester 5/Keamanan Data dan Informasi/Prak4/hidden img/hidden_img.jpg")
        
        # Validasi folder parh
        if not os.path.exists(os.path.dirname(save_path)):
            print("Folder tujuan tidak ada. Silahkan cek path yang dimasukkan")
            return

        # Simpan gambar hasil  
        secret.save(save_path)
        print(f"File berhasil disembunyikan dalam gambar. Gambar di simpan di: {save_path}")
    except Exception as e:
        print(f"Gagal menyimpan gambar: {e}")

def show_message():
    img_path = get_image_path()
    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            print(f"Pesan tersembunyi: {clear_message}")
        else:
            print("Tidak ada pesan tersembunyi dalam gambar")
    except Exception as e:
        print(f"Gagal menampilkan pesan dari gambar: {e}")


def main():
    while True:
        print("\nSteganography Tool - Terminal Version")
        print("1. Sembunyikan Pesan")
        print("2. Tampilkan Pesan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("Keluar dari program")
            break
        else:
            print("Opsi tidak valid")

if __name__ == "__main__":
    main()