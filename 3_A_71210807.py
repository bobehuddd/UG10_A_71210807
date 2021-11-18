b_06=input("Mendatar/Menurun?: ")
b_05=int(input("Masukkan kolom: "))

if b_06=="Mendatar":
    print("#"*b_05)
elif b_06=="Menurun":
    print("*\n"*b_05)
else:
    print("Pola tidak diketahui")

