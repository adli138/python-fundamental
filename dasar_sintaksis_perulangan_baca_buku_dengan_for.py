"""
Program perulangan membaca buku
"""

jumlah_buku = 23

print('Ibu berkata, "Baca Semua Bukumu, cuk" ')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print('Kemudian Adli membaca buku')
for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku+1):
    print(f"Membaca buku ke {jumlah_buku_yang_sudah_dibaca}")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')
