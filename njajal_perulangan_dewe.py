jumlah_anak = 500
jumlah_orang_tua = 300

print(fr"jumlah anak {jumlah_anak} ")
print(fr"jumlah orang tua {jumlah_orang_tua} pasang")

if jumlah_anak < jumlah_orang_tua:
    print(f"kurang {jumlah_orang_tua - jumlah_anak} anak")
if jumlah_orang_tua < jumlah_anak:
    print(f"kurang {jumlah_anak - jumlah_orang_tua} pasang orang tua")
