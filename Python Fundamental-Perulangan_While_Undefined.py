"""
Contoh perulangan dengan While
"""

Jumlah_Buku = 10
print('Ibu berkata, "Baca semua bukumu sampai paham"')
total_jumlah_baca = 0

Jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < Jumlah_Buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if Jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke { Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        Jumlah_buku_yang_sudah_dibaca_dan_dipahami = Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_dipahami } sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if total_jumlah_baca == Jumlah_Buku:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print("Bu, tidak semua buku dipahami")
