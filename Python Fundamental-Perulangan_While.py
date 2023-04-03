"""
Contoh perulangan dengan While
"""

Jumlah_Buku = 10
print('Ibu berkata, "Baca semua bukumu"')

Jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {Jumlah_buku_yang_sudah_dibaca}')

while Jumlah_buku_yang_sudah_dibaca < Jumlah_Buku:
    Jumlah_buku_yang_sudah_dibaca = Jumlah_buku_yang_sudah_dibaca + 1
    print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f'Jumlah buku yang sudah dibaca {Jumlah_buku_yang_sudah_dibaca}')
