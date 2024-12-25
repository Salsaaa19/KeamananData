from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

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
    return decrypted_text.rstrip() #Menghapus padding setelah deskripsi

plain_text = input("Masukkan teks yang ingin dienkripsi: ")
key_input = input("Masukkan key (8 karakter): ")

if len(key_input) != 8:
    raise ValueError("Key harus memiliki panjang tepat 8 karakter.")

#Konversi key ke byte
key = key_input.encode('utf-8')

#Enkripsi dan dekripsi
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)