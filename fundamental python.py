"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('ibu berkata,"Pergi ke toko"')
print('Budi menjawab,"Apa yang harus saya lakukan di toko?"')
print('Ibu mejawab, "Beli satu botol susu, jika ada telur bel1 6 "')
print("Maka budi berangkat ke toko")


# Percabangan
jumlah_botol_susu = y = 12
jumlah_telur = x = 5
print(fr"Jumlah botol susu {y} botol")
print(f'jumlah telur {jumlah_telur} butir')
if jumlah_botol_susu > 0:
    print('budi mengecek harga 1 botol susu')
    print('budi membeli 1 botol susu')
else:
    print('budi tidak jadi membeli susu')
if jumlah_telur > 6:
    print('budi membeli 6 buah telur')
if jumlah_telur > 0 < 6:
    print(f"budi membeli {x} butir telur")
else:
    print('budi hanya membeli 1 botol susu')


print('budi pulang dan menyerahkan hasil belanjaan kepada ibu')
