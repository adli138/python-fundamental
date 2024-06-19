print('\nPerintah del')
daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start end')
daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
del daftar_buku[0:2] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start end step')
daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
del daftar_buku[0::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ['Rich Dad Poor Dad', 'Crypto Trading Guide', 'Smart Money Concept', 'Pota Bee']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru2')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan list comprehension ganjil')
daftar_buku = ['1 Rich Dad Poor Dad', '2 Crypto Trading Guide', '3 Smart Money Concept', '4 Pota Bee']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan list comprehension genap')
daftar_buku = ['1 Rich Dad Poor Dad', '2 Crypto Trading Guide', '3 Smart Money Concept', '4 Pota Bee']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan list comprehension genap')
daftar_buku = ['1 Rich Dad Poor Dad', '2 Crypto Trading Guide', '3 Smart Money Concept', '4 Pota Bee']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])
