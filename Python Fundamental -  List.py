daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])


# Menampilkan list dengan "for i in range"
print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menampilkan list dengan elemen yang berbeda beda
daftar_buku = [2, 'kenji volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4Dx']
print('\nTambah 1 buku baru')  # Menambah buku di list
daftar_buku.append('Juz amma')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menghapus list
print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Mengganti Buku pertama dari Fundamental Python menjadi Eight habbits
print('\nGanti elemen pertama')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
daftar_buku[0] = 'Eight habbits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Mengambil Buku How to change your bad habbits dari list buku dengan 'pop'
print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menampilkan buku yang diambil dengan memasukkan ke  variabel baru
print('\nBuku yang diambil tadi')
print(buku)

# Mengambil buku paling ujung kanan '4DX'
print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menghilangkan buku seven habbits dengan pop -2 ( -2 dihitung dari list paling kanan )
print('\nPop -2')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
