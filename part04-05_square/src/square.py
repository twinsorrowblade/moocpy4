
def square(size, character):
    # You should call function line here with proper parameters
    size1 = size
    while size > 0:
        line(size1, character)
        size -= 1

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

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
    print()
    square(3, "o")
