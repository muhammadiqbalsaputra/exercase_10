from queue import LifoQueue

daftarPencarian = LifoQueue()
daftarPencarian2 = LifoQueue()

def hapus():
    print(f'{daftarPencarian.queue[-1]} Dihapus Dari Riwayat Pencarian')
    data = daftarPencarian.get()
    daftarPencarian2.put(data)

def menambah():
    inputPilihan1 = input('Masukan Kata Kunci Pencarian  : ')
    daftarPencarian.put(inputPilihan1)
    print(f'"{inputPilihan1}" Ditambah ke riwayat pencarian')

def undo():
    if daftarPencarian2.qsize() == 0:   
        print('Tidak ada operasi yang dapat di UNDO')
    else:
        print(f'{daftarPencarian2.queue[-1]} dikembalikan ke riwayat pencarian')
        data = daftarPencarian2.get()
        daftarPencarian.put(data)

def jarak():
    print('='*40)
    print('\n')

while True:
    print(f'Riwayat pencarian saat ini : {daftarPencarian.queue}')
    print('Pilihan : ')
    print('1. Tambahkan Pencarian')
    print('2. Hapus pencarian terakhir')
    print('3. Undo')
    print('4. Keluar')

    pilihan = input('Pilih Operasi (1 / 2 / 3 / 4) : ')

    if pilihan == '1':
        menambah()
        jarak()
    elif pilihan == '2':
        hapus()
        jarak()
    elif pilihan == '3':
        undo()
        jarak()
    elif pilihan == '4':
        print('===Terimakasih Telah Mencoba===')
        break
    else:
        print('='*30)
        print('Pilihan Tidak Ada')
        print('='*30)
        print('\n')
        