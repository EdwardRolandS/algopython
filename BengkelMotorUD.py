jwbprogram = "y"
while jwbprogram=="y" or jwbprogram=="Y":
    print ("=============================================")
    print (" CEK BIAYA PEMBELIAN OLI MOTOR BENGKEL UD ")
    print ("=============================================")
    print(" Kode = A. Duration SW20 1L")
    print(" Kode = B. Castrol Magnatec 1L")
    print(" Kode = C. Federal Supreme XX 1L")
    print(" Kode = D. Yamalube 1L")
    print(" Kode = E. Shell 1L")
    print ("=============================================")


    kode =['a','b','c','d','e']

    Merk = ['Duration SW20 1L','Castrol Magnetec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    Harga = [53000,50000,54000,45000,46000]

    pilihan = input(">> Masukkan Kode OLI = ")

#identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 0


    print(">>> Pilihan Oli      = " + Merk[idx])
    print(">>> Harga            = Rp. " + str(Harga[idx]))
    ppnawal = Harga[idx] * 0.01
    print(">>> PPN              = Rp. " + str(ppnawal))

    print("")
    jumlahbeli = input (">>> Masukan Jumlah Barang = ")

    HargaAwl= Harga[idx] * int(jumlahbeli)
    print(">> Harga Awal        = Rp. " + str(HargaAwl))

    if int(HargaAwl) >= 200000:
        potongan = int(HargaAwl) * 0.05
    elif int(HargaAwl)<200000:
        potongan = int(HargaAwl) * 0.0
    print(">> Potongan          = Rp. " + str(potongan))

    totalawal = int(HargaAwl) - int(potongan)
    print (">> Biaya Awal        = Rp. " + str(totalawal))

    totalBayar= int(totalawal) + int(ppnawal)
    print(">>> Biaya Total      = Rp. " + str(totalBayar))

    print("")
    jwbprogram = input("Menghitung Ulang ? y/t = ")
    print("")
    if jwbprogram == "T" or jwbprogram =="T":
        break
   






