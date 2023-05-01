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

# Key = id, name, username, email dll. Key harus text tidak boleh angka
# Dictionary = Python, Json = semua bahasa pemrograman
