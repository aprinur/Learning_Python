# Menghapus dengan perintah del
print('\nPerintah del')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menghapus elemen pada list dengan perintah del dan list comperhension
print('\nPerintah del dengan list comprehension')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
del daftar_buku[:]  # Format list comperhension [start:end], saat di run akan hilang semua karena start dan end kosong
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Contoh lain menghapus elemen pada list dengan perintah del dan list comperhension
print('\nPerintah del dengan list comprehension')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
del daftar_buku[0:-2]  # Format list comperhension [start:end], saat di run akan hilang elemen pertama sampai
# ketiga dari belakang
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Contoh lain menghapus elemen pada list dengan perintah del dan list comperhension
print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
del daftar_buku[0::2]  # Format list comperhension [start:end:step], saat di run akan menghapus elemen tiap 2 lompatan
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Membuat List baru dengan comperhension
print('\nMembuat lisst baru')
daftar_buku = ['Fundamental Python', 'How to change your bad habbits', 'Seven Habbits', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Menghapus List lama dan mencetak list baru dengan comperhension
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Membuat list baru dengan comperhension dan incermental
print('\nMembuat list baru dengan comperhension: ganjil')
daftar_buku = ['1 Fundamental Python', '2 How to change your bad habbits', '3 Seven Habbits', '4 4DX', ]
daftar_buku_baru = daftar_buku[0::2]  # Start:End:Step (dimulai dari nol:sampai terahkir:incremental 2)
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])
# Pencetakan dimulai dari angka variabel setelah start contoh start : 0 maka akan mulai dihitung dari list ke 1
# 0::2 = dimulai dari list ke 1 : sampai habis : lompat 2

# Membuat list baru dengan comperhension dan incermental
print('\nMembuat list baru dengan comperhension: genap')
daftar_buku = ['1 Fundamental Python', '2 How to change your bad habbits', '3 Seven Habbits', '4 4DX']
daftar_buku_baru = daftar_buku[1::2]  # Start:Stop:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Membuat list baru dengan comperhension dan incermental buang di ujung
print('\nMembuat list baru dengan comperhension: Buang di ujung')
daftar_buku = ['1 Fundamental Python', '2 How to change your bad habbits', '3 Seven Habbits', '4 4DX']
daftar_buku_baru = daftar_buku[0:-2]  # Start:Stop. [0:-2] = dimulai dari setelah 0: buang list 2 di ujung kanan
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Membuat list baru dengan comperhension dan incermental
print('\nMembuat list baru dengan comperhension: Buang diujung + step')
daftar_buku = ['1 Fundamental Python', '2 How to change your bad habbits', '3 Seven Habbits', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]  # Start:Stop:Step. [0:-1:2] = dimulai dari setelah 0: menghapus 1 diujung:
# lompat 2 kekiri. Sehingga menghapus dari belakang 1 list namun lompat 2
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Cara lain pencetakan list baru dengan comperhension dan incermental
print('\nMembuat list baru dengan comperhension: genap')
daftar_buku = ['1 Fundamental Python', '2 How to change your bad habbits', '3 Seven Habbits', '4 4DX']
print(daftar_buku[1::2])  # Start:Stop:Step

