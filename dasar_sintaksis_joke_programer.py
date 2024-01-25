"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama/ sampai kondisi terpenuhi
"""


# Sekuensial
print('Ibu berkata,"Budi, pergi ke toko"')
print('Budi berkata, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, jika ada telor beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")












