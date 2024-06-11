"""
Program perulangan membaca buku dengan while
"""

book_count = 10
print('Ibu berkata, "Baca Semua Bukumu ampe ngerti, cuk" ')
read_count = 0

understood_count = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')

print('Kemudian Adli membaca buku')
while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'Membaca Buku ke {understood_count + 1} dan belum paham')
    else:
        understood_count = understood_count + 1
        print(f"Membaca dan memahami buku ke {understood_count}")

print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print('Bu e, semua buku ku baca')
else:
    print(f'"Bu, aku gabisa paham semua bukunya, '
          f'cuma bisa paham {understood_count} buku"')