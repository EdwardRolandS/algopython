jwb = "y"
while jwb=="y" or jwb=="Y":
    print("=========================")
    print(" CEK KELULUSAN ")
    print("=========================")

    n = input("Masukkan Nilai = ")
    if int(n)>60:
        sts ="LULUS"
    else:
        sts="ULANG"
    print(sts)

#input pengulangan
    jwb= input("Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break