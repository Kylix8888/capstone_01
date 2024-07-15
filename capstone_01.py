# capstone_01.py (Mini Aplikasi)
# Studi Kasus: Data Nilai Siswa
# Variabel list dengan jangkauan global untuk menyimpan daftar nilai siswa yang di-input
# Setiap siswa akan memiliki field: nomor, nama, nilai angka, nilai huruf, dan keterangan
# Nomor siswa memiliki panjang 5 karakter dengan format S9999
# Nama siswa memiliki panjang maksimum 20 karakter
# Nilai angka di antara range 0 s.d. 100
daftar_siswa = []

# Fungsi untuk menampilkan menu utama aplikasi
def menu_utama():
    jawaban = False
    while(not(jawaban)):
        print('>>>>> Menu Utama <<<<<')
        print('----------------------')
        print('1. Input Nilai Siswa')
        print('2. Tampil Nilai Siswa')
        print('3. Update Nilai Siswa')
        print('4. Hapus Nilai Siswa')
        print('5. Keluar')
        pilihan = input('Masukkan pilihan Anda [1/2/3/4/5] : ');
        if pilihan not in ('1','2','3','4','5'):
            jawaban = False
            print('Pilihan hanya diizinkan di antara angka 1 s.d. 5.')
            print('Ulangi lagi pilihan Anda.\n')
        else:
            jawaban = True
            print()
    
    if (int(pilihan) == 1): submenu1()
    elif (int(pilihan) == 2): submenu2()
    elif (int(pilihan) == 3): submenu3()
    elif (int(pilihan) == 4): submenu4()
    else: print('Terima kasih telah menggunakan aplikasi ini.')

# Fungsi untuk mengkonversi nilai angka dari setiap siswa yang di-input menjadi nilai huruf
# Ketentuan konversi:
# 90 - 100 : A
# 80 -  89 : B
# 70 -  79 : C
# 60 -  69 : D
#  0 -  59 : E
def konversi_nilai(nilai_angka):
    nilai_huruf = ''
    if nilai_angka >= 90: nilai_huruf = 'A'
    elif nilai_angka >= 80: nilai_huruf = 'B'
    elif nilai_angka >= 70: nilai_huruf = 'C'
    elif nilai_angka >= 60: nilai_huruf = 'D'
    else: nilai_huruf = 'E'
    return nilai_huruf

# Fungsi untuk menentukan keterangan status kelulusan berdasarkan nilai huruf
# Ketentuan lulus:
# A, B, C, D: Lulus
# E: Tidak Lulus
def status_lulus(nilai_huruf):
    if nilai_huruf in ['A','B','C','D']: return 'Lulus'
    else: return 'Tidak Lulus'

# Fungsi untuk mencari siswa berdasarkan nomor siswa
def cari_siswa(nomor):
    ketemu = False
    for i in range(len(daftar_siswa)):
        if (nomor.upper() == daftar_siswa[i]['nomor']):
            ketemu = True
            break

    if (ketemu): return i+1
    else: return 0

# Fungsi untuk menampilkan daftar nilai dari semua siswa yang sudah di-input
def tampil_semua():
    if (len(daftar_siswa) == 0):
        print('Belum tersedia daftar nilai siswa.')
    else:
        print('>>>>> Daftar Nilai Siswa <<<<<')
        print('------------------------------------------------------------------')
        print('No.  | Nomor | Nama                  | Nilai | Nilai | Keterangan ')
        print('     | Siswa | Siswa                 | Angka | Huruf | ')
        print('------------------------------------------------------------------')
        for i in range(len(daftar_siswa)):
            print (' ' * (3 - len(str(i))), str(i+1), '|', daftar_siswa[i]['nomor'], '|', daftar_siswa[i]['nama'], ' ' * (20 - len(daftar_siswa[i]['nama'])), '|', ' ' * (4 - len(str(daftar_siswa[i]['nilai_angka']))), str(daftar_siswa[i]['nilai_angka']), '|', ' ' * (4 - len(daftar_siswa[i]['nilai_huruf'])), daftar_siswa[i]['nilai_huruf'], '|', daftar_siswa[i]['keterangan'])
        print('------------------------------------------------------------------')

# Fungsi untuk menampilkan submenu 1, yaitu Input Nilai Siswa
def submenu1():
    print('>>>>> Submenu Input Nilai Siswa <<<<<')
    print('-------------------------------------')
    input_lagi = True
    while(input_lagi):
        cek = True
        while (cek):
            nomor = input('Masukkan Nomor Siswa : ')
            if (len(nomor) != 5):
                print('Nomor siswa harus 5 karakter dengan format S9999. Silakan di-input ulang.')
            elif (nomor[0].upper() != 'S'):
                print('Nomor siswa harus diawali dengan huruf S dengan format S9999. Silakan di-input ulang.')
            elif (nomor[1:].isdigit() == False):
                print('Nomor siswa setelah huruf S harus berupa numerik dengan format S9999. Silakan di-input ulang.')
            else: cek = False

        cek = True
        while (cek):
            nama = input('Masukkan Nama Siswa : ')
            if (len(nama) == 0):
                print('Nama siswa minimal harus terdiri dari 1 karakter. Silakan di-input ulang.')
            else: cek = False
        
        cek = True
        while (cek):
            nilai_angka = input('Masukkan Nilai Angka : ')
            if (nilai_angka.isdigit() == False):
                print('Nilai angka harus berupa numerik dengan range 0 s.d. 100. Silakan di-input ulang.')
            elif (int(nilai_angka) < 0 or int(nilai_angka) > 100):
                print('Nilai angka harus di antara range 0 s.d. 100. Silakan di-input ulang.')
            else: cek = False

        print()

        indeks = cari_siswa(nomor)
        if (indeks != 0):
            print('Siswa dengan nomor {} sudah ada. Pastikan nomor siswa yang di-input sudah benar.\n'.format(nomor.upper()))
        else:
            siswa = dict()
            siswa['nomor'] = nomor.upper()
            if (len(nama)) > 20: siswa['nama'] = nama[0:20].capitalize()
            else: siswa['nama'] = nama.capitalize()
            siswa['nilai_angka'] = int(nilai_angka)
            siswa['nilai_huruf'] = konversi_nilai(siswa['nilai_angka'])
            siswa['keterangan'] = status_lulus(siswa['nilai_huruf'])
            daftar_siswa.append(siswa)
            print('Nilai dari siswa dengan nomor {} telah disimpan.\n'.format(siswa['nomor']))

        pilihan = True
        while(pilihan):
            lanjut = input('Apakah Anda akan meng-input nilai siswa lainnya [Y/T]? ');
            if lanjut.upper() not in ('Y', 'T'):
                print('Pilihan hanya diizinkan di antara huruf [Y]a/[T]idak.')
                print('Ulangi lagi pilihan Anda.\n')
            else:
                pilihan = False
                if (lanjut.upper() == 'Y'):
                    input_lagi = True
                else:
                    input_lagi = False
                print()

    tampil_semua()
    print()
    menu_utama()

# Fungsi untuk menampilkan submenu 2, yaitu Tampil Nilai Siswa
def submenu2():
    jawaban = False
    while(not(jawaban)):
        print('>>>>> Submenu Tampil Nilai Siswa <<<<<')
        print('--------------------------------------')
        print('1. Tampil Nilai Semua Siswa')
        print('2. Tampil Nilai Siswa Tertentu')
        print('3. Keluar ke Menu Utama')
        pilihan = input('Masukkan pilihan Anda [1/2/3] : ');

        if pilihan not in ('1','2','3'):
            jawaban = False
            print('Pilihan hanya diizinkan di antara angka 1 s.d. 3.')
            print('Ulangi lagi pilihan Anda.\n')
        elif (pilihan == '1'):
            jawaban = False
            print()
            tampil_semua()
            print()
        elif (pilihan == '2'):
            jawaban = False
            print()
            nomor = input('Masukkan Nomor Siswa : ')
            if (len(daftar_siswa) == 0):
                print('\nBelum tersedia daftar nilai siswa.\n')
            else:
                indeks = cari_siswa(nomor)
                if (indeks == 0):
                    print('\nTidak ditemukan siswa dengan nomor {}.\n'.format(nomor.upper()))
                else:
                    print('\nNilai dari siswa dengan nomor {} ({}) adalah {} ({}).\n'.format(nomor.upper(), daftar_siswa[indeks - 1]['nama'], daftar_siswa[indeks - 1]['nilai_angka'], daftar_siswa[indeks - 1]['nilai_huruf']))
        else:
            jawaban = True
            print()
            menu_utama()

# Fungsi untuk menampilkan submenu 3, yaitu Update Nilai Siswa
def submenu3():
    print('>>>>> Submenu Update Nilai Siswa <<<<<')
    print('--------------------------------------')
    nomor = input('Masukkan Nomor Siswa : ')

    if (len(daftar_siswa) == 0):
        print('\nBelum tersedia daftar nilai siswa.\n')
    else:
        indeks = cari_siswa(nomor)
        if (indeks == 0):
            print('\nTidak ditemukan siswa dengan nomor {}.\n'.format(nomor.upper()))
        else:
            nilai_angka_awal = daftar_siswa[indeks - 1]['nilai_angka'] 

            cek = True
            while (cek):
                nilai_angka_update = input('Masukkan Update Nilai Angka : ')
                if (nilai_angka_update.isdigit() == False):
                    print('Nilai angka harus berupa numerik dengan range 0 s.d. 100. Silakan di-input ulang.')
                elif (int(nilai_angka_update) < 0 or int(nilai_angka_update) > 100):
                    print('Nilai angka harus di antara range 0 s.d. 100. Silakan di-input ulang.')
                else: cek = False

            daftar_siswa[indeks - 1]['nilai_angka'] = int(nilai_angka_update)
            daftar_siswa[indeks - 1]['nilai_huruf'] = konversi_nilai(daftar_siswa[indeks - 1]['nilai_angka'])
            daftar_siswa[indeks - 1]['keterangan'] = status_lulus(daftar_siswa[indeks - 1]['nilai_huruf'])

            print('\nNilai dari siswa dengan nomor {} telah di-update.'.format(nomor.upper()))
            print('* Nilai angka sebelum di-update: {}'.format(nilai_angka_awal))
            print('* Nilai angka setelah di-update: {}'.format(daftar_siswa[indeks - 1]['nilai_angka']))
            print('* Nilai huruf setelah di-update: {}\n'.format(daftar_siswa[indeks - 1]['nilai_huruf']))
            tampil_semua()
            print()
    
    menu_utama()

# Fungsi untuk menampilkan submenu 4, yaitu Hapus Nilai Siswa
def submenu4():
    print('>>>>> Submenu Hapus Nilai Siswa <<<<<')
    print('-------------------------------------')
    nomor = input('Masukkan Nomor Siswa : ')

    if (len(daftar_siswa) == 0):
        print('\nBelum tersedia daftar nilai siswa.\n')
    else:
        indeks = cari_siswa(nomor)
        if (indeks == 0):
            print('\nTidak ditemukan siswa dengan nomor {}.\n'.format(nomor.upper()))
        else:
            del daftar_siswa[indeks - 1]
            print('\nNilai dari siswa dengan nomor {} telah dihapus.\n'.format(nomor.upper()))
            tampil_semua()
            print()
    
    menu_utama()

# Menu utama aplikasi
menu_utama()