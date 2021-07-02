print("=============================================")
print("MENU KANTIN FAKULTAS TEKNOLOGI INFORMASI")
print("=============================================")
print("MAKANAN :")
print("A. NASI GORENG       = Rp. 15.000")
print("B. Lontong Goreng    = Rp. 14.900")
print("C. Bakso Goreng      = Rp. 12.900")
print("D. Rujak Goreng      = Rp. 13.000")
print("E. Rujak Bakso       = Rp. 15.000")
print("F. Rujak Bakso Pecel = Rp. 17.000")
print()
print ("MINUMAN :")
print ("A. Teh Dingin/Hangat/Panas  = Rp. 2.500")
print ("B. Kopi Dingin              = Rp. 5.000")
print ("C. Kopi Teh Panas           = Rp. 6.500")
print ("D. Coca Cola Dingin         = Rp. 3.500")
print ("E. Coca Cola Panas          = Rp. 5.000")
print ("=============================================")

#siapkan Varibel
kodemkn =['a','b','c','d','e','f']
menumkn = ['NASI GORENG','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
hargamkn = [15000,14900,12900,13000,15000,17000]

kodeminum =['a','b','c','d','e']
menuminum =['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
hargaminum = [2500,5000,6500,3500,5000]

#input pilihan dan jumlah pemesanan
jwbprogram = "Y"
while jwbprogram=="y" or jwbprogram=="Y":
    pilihanmkn = input(">> Masukkan Menu Makanan = ")
    jumlahpesanmkn = input(">> Masukkan Jumlah Menu Makanan = ")

    i=0;
    while i<len(menumkn):
        if kodemkn[i] == pilihanmkn:
            kd_menumkn = menumkn[i]
            harga_menumkn = hargamkn[i]
        i+=1

    else: 
        pilihanminum = input(">> Masukkan Menu Minuman = ")
        jumlahpesanminum = input(">> Masukkan Jumlah Menu Minuman = ")

    o=0
    while o<len(menuminum):
        if kodeminum[o] == pilihanminum:
            kd_minum = menuminum[o]
            harga_menuminum = hargaminum[o]
        o+=1

    totalbayarmkn = int(jumlahpesanmkn) * harga_menumkn
    totalbayarminum = int(jumlahpesanminum) * harga_menuminum

    totalsemuapemesanan = totalbayarmkn + totalbayarminum
    print()
    print(">>>  Pilihan Menu Makan    = " + str(kd_menumkn))
    print(">>>  Jumlah Pesanan Makan  = " + jumlahpesanmkn)
    print(">>>  Harga Menu Makan      = Rp. " + str(harga_menumkn))
    print(">>>  Pilihan Menu Minum    = " + str(kd_minum))
    print(">>>  Jumlah Pesanan Minum  = " + str(jumlahpesanminum))
    print(">>>  Harga Menu Minum      = Rp. " + str(harga_menuminum))
    print(">>>> Total Biaya Makan     = Rp. " + str(totalbayarmkn))
    print(">>>> Total Biaya Minum     = Rp. " + str(totalbayarminum))
    print(">>>> Total Biaya Pemesanan = Rp. " + str(totalsemuapemesanan))

    jwbprogram = input ("Ingin Memesan Lagi ? y/t = ")
    if jwbprogram == "T" or jwbprogram =="t":
            break

