"""
Cek Nilai Huruf menggunakan loop
"""
#Cek Nilai Huruf
jwbulangprog = "Y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print (" ================== ")
    print (" CEK NILAI HURUF ")
    print (" ================== ")
    
    n=1
    while int(n)>0 and int(n)<=100:
        u = input("Masukkan Nilai = ")
        if int(n)>0 and int(n)<=100:
            if int(n)>=80:
                sts="Baik Sekali"
            elif int(n)>= 65: sts="Baik"
            elif int(n)>= 55: sts="Cukup"
            elif int(n)>= 40: sts="Kurang"
            else:
                sts="Kurang Sekali"
            print (sts)

            jwbulangprog = input("Ulang Program? y/t = ")
            if jwbulangprog=="t" or jwbulangprog=="T":
                break
        else:
            pesan="Masukkan Nilai 0-100 saja"
            print(pesan)
    break