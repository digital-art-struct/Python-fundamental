daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
print('Tampilkan variabele daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = (176, 'Mencari Tuhan Volume2', -345, 3,14)
print('\nTampilkan dengan for in range, dimana type data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Hijau Daun')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
daftar_buku[0] = 'Sepenggal Cerita Vol. 2'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -4')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

