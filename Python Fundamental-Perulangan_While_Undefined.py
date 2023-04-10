"""
Contoh perulangan dengan While
"""

Book_amount = 10
print('Ibu berkata, "Baca semua bukumu sampai paham"')
Readed_book = 0

Understood = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {Understood}')

while Readed_book < Book_amount * 2:
    Readed_book = Readed_book + 1
    if Understood == 9:
        print(f"Buku ke {Understood + 1} belum paham")
    else:
        Understood = Understood + 1
        print(f"Buku ke {Understood } sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {Understood}')
if Readed_book == Book_amount:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print("Bu, tidak semua buku dipahami")
