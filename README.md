# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : ELISABETH Erni Banjarnahor

Kelas : TI.24.A.5

NIM : 312410525

Mata Kuliah : Bahasa Pemograman


## mencari bilangan terbesar dari bilangan yang diinputkan
program ini menentukan bilangan terbesar dari serangkaian bilangan yang di inputkan hingga input 0. program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan. 

![foto](https://github.com/Elisabethbanjarnahor/Foto/blob/33ea8335445697fa2cfe0b33278693033a996770/IMG_20241015_125945.jpg) 


```Python```
bilangan_terbesar = 0

while True:

    bilangan = int(input("Masukkan bilangan (0 untuk berhenti): "))


    if bilangan == 0:
        break



    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan


print("Bilangan terbesar adalah:", bilangan_terbesar)


bilangan_terbesar = 0

Penjelasan: Baris ini menginisialisasi variabel bilangan_terbesar dengan nilai 0. Variabel ini akan digunakan untuk menyimpan bilangan terbesar yang dimasukkan pengguna. Kita mulai dengan nilai 0 karena kita akan membandingkan setiap bilangan yang dimasukkan dengan nilai ini.

while True:

Penjelasan: Ini adalah sebuah loop while yang akan berjalan terus-menerus selama kondisi di dalamnya bernilai True. Karena True selalu bernilai benar, maka loop ini akan berjalan tanpa henti sampai ada perintah break yang mengeksekusinya.

bilangan = int(input("Masukkan bilangan (0 untuk berhenti): "))

Penjelasan:
input("Masukkan bilangan (0 untuk berhenti): "): Baris ini menampilkan pesan ke pengguna meminta untuk memasukkan sebuah bilangan.
int(): Fungsi ini mengkonversi nilai yang dimasukkan pengguna (yang awalnya berupa string) menjadi bilangan bulat. Hasil konversi ini kemudian disimpan dalam variabel bilangan.

if bilangan == 0:

Penjelasan: Ini adalah sebuah kondisi if. Jika nilai bilangan yang dimasukkan pengguna sama dengan 0, maka kode di dalam blok if akan dijalankan.

break

Penjelasan: Jika kondisi if di atas terpenuhi (artinya pengguna memasukkan angka 0), maka perintah break akan menghentikan loop while yang sedang berjalan.

if bilangan > bilangan_terbesar:

Penjelasan: Ini adalah kondisi if kedua. Jika nilai bilangan yang baru dimasukkan lebih besar dari nilai bilangan_terbesar yang sudah tersimpan, maka kode di dalam blok if akan dijalankan.

bilangan_terbesar = bilangan

Penjelasan: Jika kondisi if di atas terpenuhi, maka nilai bilangan yang baru (yang lebih besar) akan disimpan ke dalam variabel bilangan_terbesar, menggantikan nilai sebelumnya.

print("Bilangan terbesar adalah:", bilangan_terbesar)

Penjelasan: Setelah loop while selesai (karena pengguna memasukkan angka 0 atau karena alasan lain), baris ini akan mencetak ke layar pesan yang menunjukkan bilangan terbesar yang telah ditemukan.
