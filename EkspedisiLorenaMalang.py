
jwbprogram = "y"
while jwbprogram=="y" or jwbprogram=="Y":
    print ("=============================================")
    print(" TRANSKASI BIAYA EKSPEDISI ")
    print ("=============================================")
    print(" Kode = A. Surabaya")
    print(" Kode = B. Bandung")
    print ("=============================================")
    
    kode =['a','b']
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]



#identifikasi pilihan


    pilihan = input(">> Masukkan Kode Tujuan = ")
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 0
        

#cetak tampilan layar
    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

    #hitung transksi
    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    #tampilkan total ongkir
    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))

    jwbprogram = input("Menghitung Ulang ? y/t = ")
    if jwbprogram == "T" or jwbprogram =="T":
        break