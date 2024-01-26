"""
Program perulangan membaca buku dengan While sampai mahir
"""
book_count = 10
print('Ibu berkata, "Baca semua bukumu"')
read_count = 0


understood_count = 0
print(f'Jumlah_buku_yang_sudah_dibaca_dan_dipahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke{understood_count + 1} belum_paham")
    else:
        understood_count = understood_count + 1
        print(f'Buku ke {understood_count} sudah dibaca_dan_dipahami')

print(f'Jumlah_buku_yang_sudah_dibaca_dan_dipahami {understood_count}')
if understood_count == book_count:
    print("Bu, semua buku sudah dibaca dan dipahami ")
else:
    print(f"Bu, tidak semua buku bisa dipahami, "
          f"Budi hanya bisa memahami {understood_count} buku")



