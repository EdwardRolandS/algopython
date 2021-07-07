import datetime
from time import process_time_ns

x = datetime.datetime.now()
jwbprogram="y"
while jwbprogram=="y" or jwbprogram=="Y":
    print("========================================================")
    print("                     input Slip Gaji                  ")
    print("                   Tanggal : ",x.strftime("%x"))
    print("========================================================")

    nama = input("Nama                          = ")

    #1.identifikasi gaji, golongan dan tunjangan istri
    gajipokok= ['2500000','4500000','6500000']
    golongan = ['1','2','3']
    gol = input("Golongan                      = ")
    golinput = int(gol)

    if golinput == 1:
        idx = 0
        tunjangan = 0.01
    elif golinput == 2:
        idx = 1
        tunjangan = 0.03
    elif golinput == 3:
        idx = 2
        tunjangan = 0.05
    else:
        print ("Golongan Terdaftar Hanya 1 sampai 3")

    #identifikasi kelamin, status dan anak
    kelamin = input("Jenis Kelamin (laki laki/perempuan) = ")
    status = input("Status (Kawin/Belum)                = ")
    anak = input("Memiliki Anak (iya/tidak)           = ")

    #2. Tunjangan Istri
    if kelamin=="laki laki" or kelamin=="Laki laki" or kelamin=="laki-laki" or kelamin=="Laki-laki" and status == "kawin" or status=="Kawin":
        tunjanganistri = int(gajipokok[idx]) * tunjangan 
    else :
        tunjanganistri = 0

    #3. Tunjangan Anak
    if status == "kawin" or status=="Kawin" and anak == "iya" or anak == "Iya":
        tunjangananak = int(gajipokok[idx]) * 0.02
    else:
        tunjangananak = 0

    #4. Gaji Bruto
    gajibruto = int(gajipokok[idx]) + int(tunjanganistri) + int(tunjangananak)

    #5. Biaya Jabatan
    biayajabatan = int(gajibruto)
    iuranpensiun = 15500
    iuranorganisasi = 3500
    gajinetto = int(gajibruto) - int(iuranorganisasi) - int(iuranpensiun)

    print()
    print()
    print("========================================================")
    print("                     input Slip Gaji                  ")
    print("                   Tanggal : ",x.strftime("%x")        )
    print("========================================================")
    print()
    print("Nama                     " + nama)
    print("Golongan                 " + str(golinput))
    print("jenis kelamin            " + kelamin)
    print("Staus Kawin              " + status)
    print("Gaji Pokok               " + gajipokok[idx])
    print("Tunjangan istri          " + str(tunjanganistri))
    print("Tunjangan Anak           " + str(tunjangananak))
    print(">>Gaji bruto             " + str(gajibruto))
    print("========================================================")
    print("Biaya Jabatan            " + str(biayajabatan))
    print("Iuran Pensiun            " + str(iuranpensiun))
    print("Iuran Organisasi         " + str(iuranorganisasi))
    print(">>Gaji Netto             " + str(gajinetto))
    print()

    jwbprogram = input("Ulang Menghitung ? y/t = ")
    print()
    if jwbprogram=="t" or jwbprogram=="T":
        break
