daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
print('Tampilkan Daftar Buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[3])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTambahkan 1 Buku baru')
daftar_buku.append('Indomaret')
print(daftar_buku[4])

print('\nTampilkan Seluruh Daftar buku')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list daftar buku')
daftar_buku.clear()

daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
daftar_buku.append('Indomaret')

print('\nMengganti Judul buku pertama')
daftar_buku[0] = 'Estimasi Biaya'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengambil Elemen ke 3')
buku = daftar_buku.pop(3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenampilkan Elemen yang diambil')
print(buku)

daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
daftar_buku.append('Indomaret')

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
daftar_buku.append('Indomaret')
print('\nPop -2')
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

