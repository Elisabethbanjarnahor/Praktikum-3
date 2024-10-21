def bilangan_terbesar(a, b, c):
  """Fungsi untuk mencari bilangan terbesar dari tiga bilangan"""

 
  terbesar = a

  
  if b > terbesar:
    terbesar = b

  
  if c > terbesar:
    terbesar = c

  return terbesar


bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))


hasil = bilangan_terbesar(bilangan1, bilangan2, bilangan3)
print("Bilangan terbesar adalah:", hasil)
