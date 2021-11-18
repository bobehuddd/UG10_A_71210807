nilaiug=float(input("Masukkan nilai rata-rata UG anda: "))
nilaitts=float(input("Masukkan nilai TTS anda: "))
nilaitas=float(input("Masukkan nilai TAS anda: "))
aveug=nilaiug*(70/100)
avetts=nilaitts*(15/100)
avetas=nilaitas*(15/100)
totalnilai=aveug+avetas+avetts
print("=========================")
print("Nilai anda: ",totalnilai)
if(totalnilai>=85):
    tingkat="A"
elif(totalnilai>=80):
    tingkat="A-"
elif(totalnilai>=75):
    tingkat="B+"
elif(totalnilai>=70):
    tingkat="B"
elif(totalnilai>=65):
    tingkat="B-"
elif(totalnilai>=60):
    tingkat="C+"
elif(totalnilai>=55):
    tingkat="C"
elif(totalnilai>=45):
    tingkat="D"
else:
    tingkat="E"
print("Nilai huruf anda: ",tingkat)