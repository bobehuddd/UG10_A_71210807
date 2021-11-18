print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
pilihansaya=int(input("Masukkan menu yang anda pilih: "))
if(pilihansaya==1):
    cantik1=float(input("Masukkan bilangan yang ingin dibagi: "))
    cantik2=float(input("Masukkan bilangan pembagi: "))
    jumlah=cantik1%cantik2
    print("Sisa hasil bagi",cantik1,"dibagi dengan",cantik2,"adalah",jumlah)
elif(pilihansaya==2):
    cantik1=float(input("Masukkan bilangan yang ingin dibagi: "))
    cantik2=float(input("Masukkan bilangan pembagi: "))
    jumlah=cantik1/cantik2
    print("Hasil pembagian",cantik1,"dibagi dengan",cantik2,"dibulatkan kebawah adalah",jumlah)
elif(pilihansaya==3):
    cantik1=float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    jumlah=cantik1**(1/3)
    print("Akar kubik dari",cantik1,"adalah",jumlah)
else:
    print("Menu yang anda pilih tidak tersedia")
    