

# Mendefinisikan fungsi dengan nama 'box_of_hashes' yang menerima satu parameter 'height'
def box_of_hashes(height):
    # Menggunakan perulangan while yang akan berjalan selama nilai 'height' lebih dari 0
    while height > 0:
        # Memanggil fungsi 'line' dengan argumen 'height' sebagai panjang, 10 sebagai lebar, dan "#" sebagai karakter yang akan dicetak
        line(10, "#")
        # Mengurangi nilai 'height' sebanyak satu setiap kali loop berjalan, sehingga mengurangi tinggi kotak yang dicetak
        height -= 1

# Mendefinisikan fungsi dengan nama 'line' yang menerima tiga parameter: 'height', 'p', dan 'q'
def line(p, q):
    # Mengecek apakah string 'q' kosong
    if q == "":
        # Jika 'q' kosong, mencetak '*' sebanyak 'p' kali
        print("*" * p)
    # Mengecek apakah panjang string 'q' lebih dari 0
    elif len(q) > 0:
        # Jika panjang 'q' lebih dari 0, mencetak karakter pertama dari 'q' sebanyak 'p' kali
        print(q[0] * p)
    # Jika kondisi lain tidak terpenuhi
    else:
        # Mencetak seluruh string 'q' sebanyak 'p' kali
        print(q * p)

# Blok kode ini akan dieksekusi hanya jika file ini dijalankan sebagai script utama, bukan sebagai modul
if __name__ == "__main__":
    # Memanggil fungsi 'box_of_hashes' dengan argumen 5, yang berarti akan mencetak kotak dari simbol "#" dengan tinggi 5
    box_of_hashes(5)
