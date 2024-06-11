"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 100
print('Ibu berkata, "Baca Semua Bukumu, cuk" ')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print('Kemudian Adli membaca buku')
while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"Membaca buku ke {jumlah_buku_yang_sudah_dibaca}")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')