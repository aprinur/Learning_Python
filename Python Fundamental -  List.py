daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])


print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [2, 'kenji volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits']
print('\nTambah 1 buku baru')
daftar_buku.append('Juz amma')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
