"""
Contoh perulangan dengan While
"""

Jumlah_Buku = 10
print('Ibu berkata, "Baca semua bukumu sampai paham"')
Jumlah_baca = 0

Jumlah_paham = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_paham}')

while Jumlah_baca < Jumlah_Buku * 2:
    Jumlah_baca = Jumlah_baca + 1
    if Jumlah_paham == 9:
        print(f"Buku ke {Jumlah_paham + 1} belum paham")
    else:
        Jumlah_paham = Jumlah_paham + 1
        print(f"Buku ke {Jumlah_paham } sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_paham}')
if Jumlah_baca == Jumlah_Buku:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print("Bu, tidak semua buku dipahami")
