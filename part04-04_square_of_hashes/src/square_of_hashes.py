# Mendefinisikan fungsi dengan nama 'square_of_hashes' yang menerima satu parameter 'main'
def square_of_hashes(main):
    # Menyimpan nilai awal 'main' untuk mengontrol lebar dari setiap baris
    initial_width = main
    # Menggunakan perulangan while yang akan berjalan selama nilai 'main' lebih dari 0
    while main > 0:
        # Memanggil fungsi 'line' dengan argumen 'initial_width' sebagai lebar, dan "#" sebagai karakter yang akan dicetak
        line(initial_width, "#")
        # Mengurangi nilai 'main' sebanyak satu setiap kali loop berjalan, sehingga mengurangi tinggi kotak yang dicetak
        main -= 1

# Mendefinisikan fungsi dengan nama 'line' yang menerima dua parameter: 'p' dan 'q'
def line(p, q):
    # Mengecek apakah string 'q' kosong
    if q == "":
        # Jika 'q' kosong, mencetak '*' sebanyak 'p' kali
        print("*" * p)
    elif len(q) > 0:
        # Jika panjang 'q' lebih dari 0, mencetak karakter pertama dari 'q' sebanyak 'p' kali
        print(q[0] * p)
    else:
        # Mencetak seluruh string 'q' sebanyak 'p' kali
        print(q * p)

# Blok kode ini akan dieksekusi hanya jika file ini dijalankan sebagai script utama, bukan sebagai modul
if __name__ == "__main__":
    # Memanggil fungsi 'square_of_hashes' dengan argumen 5, yang berarti akan mencetak kotak dari simbol "#" dengan tinggi 5 dan lebar 5
    square_of_hashes(5)
    print()  # Mencetak baris kosong antara dua output
    # Memanggil fungsi 'square_of_hashes' dengan argumen 3, yang berarti akan mencetak kotak dari simbol "#" dengan tinggi 3 dan lebar 3
    square_of_hashes(3)
