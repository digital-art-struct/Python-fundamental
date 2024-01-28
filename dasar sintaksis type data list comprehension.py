print('\nPerintah del')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
del daftar_buku[ : ]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Sepenggal Cerita', 'Hidup Bermanfaat', 'Demi Masa', 'Gelap']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension ganjil')
daftar_buku = ['1 Sepenggal Cerita', '2 Hidup Bermanfaat', '3 Demi Masa', '4 Gelap']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension genap')
daftar_buku = ['1 Sepenggal Cerita', '2 Hidup Bermanfaat', '3 Demi Masa', '4 Gelap']
daftar_buku_baru = daftar_buku[1::2] #START:STOP;END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension buang diujung')
daftar_buku = ['1 Sepenggal Cerita', '2 Hidup Bermanfaat', '3 Demi Masa', '4 Gelap']
daftar_buku_baru = daftar_buku[0:-1] #START:STOP;END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension buang diujung lompat 2')
daftar_buku = ['1 Sepenggal Cerita', '2 Hidup Bermanfaat', '3 Demi Masa', '4 Gelap']
daftar_buku_baru = daftar_buku[0:-1:2] #START:STOP;END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension ganjil bisa juga begini')
daftar_buku = ['1 Sepenggal Cerita', '2 Hidup Bermanfaat', '3 Demi Masa', '4 Gelap']
print (daftar_buku[0::2])

