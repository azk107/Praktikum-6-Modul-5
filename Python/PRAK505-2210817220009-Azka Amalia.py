def Biodata(tahunLahir,nama,asal):
    tahunLahir = int(tahunLahir)
    tahun_sekarang = 2020
    print("Perkenalkan Nama Saya : ", nama)
    print("Umur Saya : ", tahun_sekarang-tahunLahir)
    print("Saya Adalah Angkatan : ", tahun_sekarang)
    print("Asal Saya dari : ", asal)
tahunLahir = int(input())
A = input()
B = input()
Biodata(tahunLahir, A, B)