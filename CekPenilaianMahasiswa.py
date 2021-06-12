print ("=============")
print ("Cek Nilai Mahasiswa")
print ("================")

n=input("Masukan Nilai = ")

if int(n)>0 and int(n)<=100:
    if int(n)>=91: sts="A"
    elif int(n)>=81: sts="B"
    elif int(n)>=71: sts="C"
    else:
        sts=("D")
    print(sts)
else:
    pesan= "Masukan Nilai Mahasiswa 0-100 Saja"
    print(pesan)