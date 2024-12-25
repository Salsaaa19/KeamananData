class Enigma:
    def __init__(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        # Rotor dan reflektor
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        # Posisi awal rotor
        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

        # Invers rotor untuk proses dekripsi
        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        """Membuat rotor invers untuk proses dekripsi."""
        inverse_rotor = [0] * 26
        for i in range(26):
            inverse_rotor[rotor[i]] = i
        return inverse_rotor
    
    def encrypt_decrypt_char(self, ch):
        """Enkripsi atau dekripsi satu karakter."""
        if ch.isalpha():
            is_lower = ch.islower()
            ch = ch.upper()

            offset = ord(ch) - ord('A')

            # Rotor maju
            offset = (self.rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26
            offset = (self.rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26

            # Reflektor
            offset = self.reflector[offset]

            # Rotor mundur (invers)
            offset = (self.inverse_rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26
            offset = (self.inverse_rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.inverse_rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26

            # Rotasi rotor setelah setiap karakter
            self.rotor1_pos = (self.rotor1_pos + 1) % 26
            if self.rotor1_pos == 0:
                self.rotor2_pos = (self.rotor2_pos + 1) % 26
                if self.rotor2_pos == 0:
                    self.rotor3_pos = (self.rotor3_pos + 1) % 26

            result = chr(offset + ord('A'))
            return result.lower() if is_lower else result
        else:
            return ch # Mengembalikan karakter jika bukan huruf
        
    def process(self, text):
        """Memproses string untuk enkripsi adau dekripsi."""
        result = ''.join(self.encrypt_decrypt_char(ch) for ch in text)
        return result

# Inisialisasi posisi rotor
rotor1_pos = 0
rotor2_pos = 0
rotor3_pos = 0

enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)

# Enkripsi
input_text = input("Masukkan teks yangn akan dienkripsi: ")
encrypted_text = enigma.process(input_text)
print("Teks terenkripsi:", encrypted_text)

# Reset posisi rotor untuk dekripsi
enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
decrypted_text = enigma.process(encrypted_text)
print("Teks terdekripsi:", decrypted_text)
