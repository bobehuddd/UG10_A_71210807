Artikelx1 = input("Masukkan artikel yang ingin dipindai: ")
Klubx1 = input("Masukkan nama klub favorit anda: ")
Skorx1 = input("Masukkan score yang ingin dicari: ")
if (Skorx1 and Klubx1) in Artikelx1:
    print("Hasil pencarian ditemukan")
elif Skorx1 in Artikelx1:
    print("Hanya skor {} yang ditemukan pada artikel ini".format(Skorx1))
elif Klubx1 in Artikelx1:
    print("Hanya kata {} yang ditemukan pada artikel ini".format(Klubx1))
else:
    print("Hasil pencarian {} dan {} tidak ditemukan".format(Klubx1,Skorx1))
