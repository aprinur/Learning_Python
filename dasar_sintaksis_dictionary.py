# Tipe data dictionary

users = {   # Penulisan dictionary menggunakan kurung kurawal
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "City": "Gwenborough",
        "Zipcode": "92998-3874",
        "Geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)  # Contoh kode untuk menampilkan seluruh isi dictionary
print(users["id"])
print(users["name"])
print(users["username"])   # Contoh kode untuk menampilkan salah 1 isi dictionary,id bisa diganti key yang lain
print(users["email"])
print(users["address"]["City"])
print(users["address"]["Geo"]["lng"])  # Contoh kode untuk menampilkan isi dictionary yang lebih spesifik

# Contoh penggunaan json.dumps
print(users)  # Hasil cetak akan menggunakan petik 1 berdasakan standart python
print(type(users))  # Kode untuk cek tipe data
print('\nUbah Dictionary ke Json')
import json  # Kode untuk mengubah Dictionary ke Json berupa string
result = json.dumps(users)
print(type(result))
print(result)    # Hasil cetak akan menggunakan petik 2

# Contoh penggunaan json.dump
with open('result.json', 'w') as file:  # Contoh membuka file di python dengan perintah open. 'w' = write
    json.dump(users, file)  # Saat dijalankan akan ada file baru bernama result.json

# Key = id, name, username, email dll. Key harus text tidak boleh angka
# Dictionary = Python, Json = semua bahasa pemrograman
# Dictionary tidak sama dengan Json meski bentuknya sama
# Str = String
# Dict = Dictionary
# Dumps = Mengubah ke string
# Dump = Mengubah ke file
# Untuk mengubah tampilan file gunakan fungsi "reformat code" pada tab "code"
