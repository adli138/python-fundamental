"""

1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali kali selama/ sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Tolong ke Toko Sembako"')
print('Adli menjawab, "Oke ma, apa yang harus saya lakukan?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka Adli berangkat ke toko")
print("dan mulai berbelanja")

# Percabangan
milk_bottle_count = 123012
if milk_bottle_count > 0:
    print('Adli mengecek harganya, dan ternyata uang nya cukup')
    print('Adli membeli 5 botol susu')
else:
    print('Adli gak jadi beli susu')

print('Adli pulang ke rumah')
print('Menyampaikan belanjaannya kepada ibu')