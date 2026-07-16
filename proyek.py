# STRUKTUR DATA:
# 1. Linked List
# 2. Queue
# 3. Dictionary
# 4. file txt
class NodeKegiatan:
    def __init__(self, nama, tanggal, pj, jenis):
        self.nama = nama
        self.tanggal = tanggal
        self.pj = pj
        self.jenis = jenis
        self.next = None
        
class LinkedListKegiatan:
    def __init__(self):
        self.head = None
    # tambah kegiatan
    def tambah_kegiatan(self, nama, tanggal, pj, jenis):
        node_baru = NodeKegiatan(nama,tanggal,pj,jenis)

        if self.head is None:
            self.head = node_baru
        else:
            kegiatan = self.head
            while kegiatan.next:
                kegiatan = kegiatan.next
            kegiatan.next = node_baru
    # tampilkan kegiatan
    def tampilkan_kegiatan(self):       
        print("\n===== DATA KEGIATAN =====")
        if self.head is None:
            print("\nBelum ada kegiatan yang terdaftar!")
            return
        kegiatan=self.head
        nomor = 1

        while kegiatan:
            print(f"\n{nomor}.Kegiatan : {kegiatan.nama}")
            print(f"   Tanggal  : {kegiatan.tanggal}")
            print(f"   PJ       : {kegiatan.pj}")
            print(f"   Jenis    : {kegiatan.jenis}")
            kegiatan = kegiatan.next
            nomor += 1

    # cari nama kegiatan
    def cari_nama(self, nama):
        kegiatan = self.head
        ditemukan = False
        while kegiatan:
            if nama.strip() == "":
                print("\nNama kegiatan tidak boleh kosong!")
                return
            if nama.lower() in kegiatan.nama.lower():
                print("\nDATA DITEMUKAN")
                print(f"Nama      : {kegiatan.nama}")
                print(f"Tanggal   : {kegiatan.tanggal}")
                print(f"PJ        : {kegiatan.pj}")
                print(f"Jenis     : {kegiatan.jenis}")

                ditemukan = True
            kegiatan = kegiatan.next
        if ditemukan == False: 
            print("\nKegiatan tidak ditemukan!")
    
    # cari tanggal
    def cari_tanggal(self, tanggal):       
        if tanggal.count("-") != 2:
            print("\nFormat tanggal harus DD-MM-YYYY")
            return
        kegiatan = self.head
        ditemukan = False
        while kegiatan:
            if kegiatan.tanggal == tanggal:
                print("\nDATA DITEMUKAN")
                print(f"Nama      : {kegiatan.nama}")
                print(f"Tanggal   : {kegiatan.tanggal}")
                print(f"PJ        : {kegiatan.pj}")
                print(f"Jenis     : {kegiatan.jenis}")
                ditemukan = True
            kegiatan = kegiatan.next
        if ditemukan == False:
            print("\nData tidak ditemukan!")

# =========================================
# QUEUE EVALUASI
# =========================================
class QueueEvaluasi:
    def __init__(self):
        self.queue = []
    # enqueue
    def enqueue(self, data):
        self.queue.append(data)
    # tampilkan data evaluasi
    def tampilkan(self):
        print("\n===== DATA EVALUASI =====")
        if len(self.queue) == 0:
            print("\nBelum ada data evaluasi!")
            return
        nomor = 1
        for data in self.queue:
            print(f"\n{nomor}.")
            print(f"NIM       : {data['nim']}")
            print(f"Nama      : {data['nama']}")
            print(f"Kegiatan  : {data['kegiatan']}")
            nomor += 1
            
class DataMahasiswa:
    def __init__(self):
        self.data = {}
    # tambah mahasiswa
    def tambah_mahasiswa(self, nim, nama):
        self.data[nim] = nama
    # cari mahasiswa
    def cari_mahasiswa(self, nim):
        if nim in self.data:
            print("\n===== DATA MAHASISWA =====")
            print(f"NIM   : {nim}")
            print(f"Nama  : {self.data[nim]}")
            jumlah_kegiatan = 0
            daftar_kegiatan = []
            # ambil data dari evaluasi
            for data in data_evaluasi.queue:
                if data["nim"] == nim:
                    kegiatan = data["kegiatan"].split("|")
                    jumlah_kegiatan += len(kegiatan)

                    for item in kegiatan:
                        daftar_kegiatan.append(item)
            print(f"Jumlah kegiatan : {jumlah_kegiatan}")
            if jumlah_kegiatan > 0:
                print("Kegiatan yang diikuti :")
                nomor = 1
                for kegiatan in daftar_kegiatan:
                    print(f"{nomor}. {kegiatan}")
                    nomor += 1
            else:

                print("Belum mengikuti kegiatan")
        else:
            print("\nMahasiswa tidak ditemukan!")

    # tampilkan semua mahasiswa
    def tampilkan_semua(self):
        print("\n===== DATA MAHASISWA =====")
        nomor = 1
        for nim, nama in self.data.items():
            print(f"{nomor}. {nim} - {nama}")
            nomor += 1
            
# MEMBUAT OBJECT

data_kegiatan = LinkedListKegiatan()
data_mahasiswa = DataMahasiswa()
data_evaluasi = QueueEvaluasi()

# MEMBACA FILE mahasiswa.txt

with open("mahasiswa.txt", "r") as file:
    for baris in file:
        baris = baris.strip()
        if baris != "":
            bagian = baris.split(",")
            if len(bagian) != 2:
                continue
            nim = bagian[0]
            nama = bagian[1]
            data_mahasiswa.tambah_mahasiswa(nim,nama )

# MEMBACA FILE kegiatan.txt
with open("kegiatan.txt", "r") as file:
    for baris in file:
        baris = baris.strip()
        if baris != "":
            bagian = baris.split(",")
            if len(bagian) != 4:
                continue
            nama = bagian[0]
            tanggal = bagian[1]
            pj = bagian[2]
            jenis = bagian[3]
            data_kegiatan.tambah_kegiatan(nama, tanggal, pj, jenis)

# MEMBACA FILE evaluasi.txt

with open("evaluasi.txt", "r") as file:
    for baris in file:
        baris = baris.strip()
        if baris != "":
            bagian = baris.split(",")
            if len(bagian) != 3:
                continue
            nim = bagian[0]
            nama = bagian[1]
            kegiatan = bagian[2]
            data = {"nim": nim,"nama": nama,"kegiatan": kegiatan}
            data_evaluasi.enqueue(data)

# TAMBAH KEGIATAN BARU
# otomatis masuk kegiatan.txt

def tambah_kegiatan_baru():
    print("\n===== TAMBAH KEGIATAN =====")
    nama = input("Nama kegiatan       : ").strip()
    tanggal = input("Tanggal             : ").strip()
    pj = input("PJ (Kementrian)     : ").strip()
    jenis = input("Jenis kegiatan      : ").strip()

    # cek input kosong
    if (
        nama.strip() == ""
        or tanggal.strip() == ""
        or pj.strip() == ""
        or jenis.strip() == ""
    ):
        print("\nSemua field haus diisi!")
        return

    # cek tanggal angka
    if tanggal.count("-") != 2:
        print("\nFormat tanggal harus DD-MM-YYYY")
        return
    # cek kegiatan sudah ada
    data_sekarang = data_kegiatan.head
    while data_sekarang:
        if nama.lower() == data_sekarang.nama.lower():
            print("\nKegiatan sudah terdaftar!")
            return
        elif tanggal == data_sekarang.tanggal:
            print("\nsudah ada kegiatan tanggal tersebut!")
            return
        data_sekarang = data_sekarang.next
    # tambah ke linked list
    data_kegiatan.tambah_kegiatan(nama,tanggal,pj,jenis)
    # simpan ke file txt
    with open("kegiatan.txt", "a") as file:

        file.write(f"\n{nama},{tanggal},{pj},{jenis}")
    print("\nKegiatan berhasil ditambahkan!")

# TAMBAH MAHASISWA BARU
# otomatis masuk mahasiswa.txt

def tambah_mahasiswa_baru():
    print("\n===== TAMBAH MAHASISWA =====")
    nim = input("Masukkan NIM  : ").strip()
    nama = input("Masukkan Nama : ").strip()

    # cek NIM sudah ada
    if nama.strip() == ""and nim.strip() == "":
        print("\nNIM dan Nama tidak boleh kosong!")
        return
    if nama.strip() == "":
        print("\nNama tidak boleh kosong!")
        return
    if not nim.isdigit():
        print("\nNIM harus berupa angka/NIM tidka boleh kosong!")
        return
    if nim in data_mahasiswa.data:
        print("\nNIM sudah terdaftar, silahkan gunakan NIM lain!")
        return

    for nama_mahasiswa in data_mahasiswa.data.values():
        if nama.lower() == nama_mahasiswa.lower():
            print("\nNama sudah terdaftar, silahkan gunakan nama lain!")
            return

    # cek input kosong
    if nim.strip() == "" or nama.strip() == "":
        print("\nNIM dan Nama tidak boleh kosong!")
        return
    # tambah data
    data_mahasiswa.tambah_mahasiswa(nim,nama)
    # simpan ke txt
    with open("mahasiswa.txt", "a") as file:
        file.write(f"\n{nim},{nama.upper()}")
    print("\nMahasiswa berhasil ditambahkan!")


# TAMBAH PESERTA KEGIATAN
# otomatis masuk evaluasi.txt

def tambah_peserta():
    print("\n===== TAMBAH PESERTA =====")

    while True:
        nim = input("Masukkan NIM : ").strip()
        if nim == "":
            print("\nNIM tidak boleh kosong!")
            continue
        if nim not in data_mahasiswa.data:
            print("\nNIM tidak ditemukan!")
            continue
        break
    nama = data_mahasiswa.data[nim]
    daftar_kegiatan = []

    while True:
        kegiatan = input("\nMasukkan nama kegiatan : ").strip()

        if kegiatan == "":
            print("\nNama kegiatan tidak boleh kosong!")
            continue

        # cek kegiatan ada di linked list
        cek = data_kegiatan.head
        ditemukan = False

        while cek:
            if kegiatan.lower() == cek.nama.lower():
                ditemukan = True
                break
            cek = cek.next

        if not ditemukan:
            print("\nKegiatan tidak ditemukan!")
            continue
        # cek apakah mahasiswa sudah mengikuti kegiatan
        sudah_ikut = False
        for data in data_evaluasi.queue:
            if data["nim"] == nim:
                kegiatan_lama = data["kegiatan"].split("|")
                for item in kegiatan_lama:
                    if kegiatan.lower() == item.lower():
                        sudah_ikut = True
                        break


        if sudah_ikut:
            print("\nMahasiswa sudah mengikuti kegiatan tersebut, silakan pilih kegiatan lain!")
            continue
        # cegah duplikat dalam input yang sama
        if kegiatan in daftar_kegiatan:
            print("\nKegiatan sudah dipilih!")
            continue
        daftar_kegiatan.append(kegiatan)
        lagi = input("Tambah kegiatan lagi? (y/t) : ").strip()
        if lagi.lower() != "y":
            break
        
    # cek apakah NIM sudah ada di evaluasi
    for data in data_evaluasi.queue:
        if data["nim"] == nim:
            kegiatan_lama = data["kegiatan"].split("|")
            for kegiatan_baru in daftar_kegiatan:
                if kegiatan_baru not in kegiatan_lama:
                    kegiatan_lama.append(kegiatan_baru)
            data["kegiatan"] = "|".join(kegiatan_lama)
            with open("evaluasi.txt", "w") as file:
                data_baru = []
                for item in data_evaluasi.queue:
                    data_baru.append(f"{item['nim']},{item['nama']},{item['kegiatan']}")
                file.write("\n".join(data_baru))
            print("\n kegiatan berhasil ditambahkan!")
            return

    # jika NIM belum ada di evaluasi
    hasil_kegiatan = "|".join(daftar_kegiatan)
    data = {"nim": nim,"nama": nama,"kegiatan": hasil_kegiatan}
    data_evaluasi.enqueue(data)
    with open("evaluasi.txt", "a") as file:
        file.write(f"\n{nim},{nama},{hasil_kegiatan}")
    print("\nPeserta berhasil ditambahkan!")
    
def statistik():
    print("========== STATISTIK =============")

    
    # HITUNG KEGIATAN PALING DIMINATI
   
    hitung_kegiatan = {}

    for data in data_evaluasi.queue:
        daftar_kegiatan = data["kegiatan"].split("|")

        for kegiatan in daftar_kegiatan:
            kegiatan = kegiatan.strip()
            # cek apakah kegiatan ada di linked list
            cek = data_kegiatan.head
            valid = False
            while cek:
                if kegiatan.lower() == cek.nama.lower():
                    valid = True
                    break
                cek = cek.next

            if not valid:
                continue
            if kegiatan in hitung_kegiatan:
                hitung_kegiatan[kegiatan] += 1
            else:
                hitung_kegiatan[kegiatan] = 1

    if len(hitung_kegiatan) == 0:
        print("\nBelum ada kegiatan yang valid!")
        return

    list_kegiatan = []

    for kegiatan, jumlah in hitung_kegiatan.items():
        list_kegiatan.append([kegiatan, jumlah])

    # sorting descending
    for i in range(len(list_kegiatan)):
        for j in range(i + 1, len(list_kegiatan)):
            if list_kegiatan[j][1] > list_kegiatan[i][1]:
                list_kegiatan[i], list_kegiatan[j] = list_kegiatan[j], list_kegiatan[i]

    print("\n===== 3 KEGIATAN PALING DIMINATI =====\n")

    nomor = 1
    for data in list_kegiatan[:3]:
        print(f"{nomor}. {data[0]} ({data[1]} mahasiswa)")
        print(f"Nama mahasiswa yang mengikuti {data[0]} :")

        for peserta in data_evaluasi.queue:
            daftar = peserta["kegiatan"].split("|")

            for item in daftar:
                if item.strip().lower() == data[0].lower():
                    print(f"- {peserta['nama']}_{peserta['nim']}")

        print()
        nomor += 1

    # =====================================
    # HITUNG MAHASISWA PALING AKTIF
    # =====================================
    hitung_mahasiswa = {}

    for data in data_evaluasi.queue:

        jumlah_kegiatan_valid = 0

        daftar_kegiatan = data["kegiatan"].split("|")

        for kegiatan in daftar_kegiatan:
            kegiatan = kegiatan.strip()
            cek = data_kegiatan.head
            valid = False

            while cek:
                if kegiatan.lower() == cek.nama.lower():
                    valid = True
                    break
                cek = cek.next
            if valid:
                jumlah_kegiatan_valid += 1

        hitung_mahasiswa[data["nama"]] = jumlah_kegiatan_valid
    list_mahasiswa = []

    for nama, jumlah in hitung_mahasiswa.items():
        list_mahasiswa.append([nama, jumlah])

    # sorting descending
    for i in range(len(list_mahasiswa)):
        for j in range(i + 1, len(list_mahasiswa)):
            if list_mahasiswa[j][1] > list_mahasiswa[i][1]:
                list_mahasiswa[i], list_mahasiswa[j] = list_mahasiswa[j], list_mahasiswa[i]

    print("===== 3 MAHASISWA PALING AKTIF =====\n")

    nomor = 1
    for data in list_mahasiswa[:3]:
        print(f"{nomor}. {data[0]} ({data[1]} kegiatan)")
        print(f"Kegiatan yang diikuti {data[0]} :")

        for peserta in data_evaluasi.queue:

            if peserta["nama"] == data[0]:
                daftar_kegiatan = peserta["kegiatan"].split("|")
                for kegiatan in daftar_kegiatan:
                    kegiatan = kegiatan.strip()
                    cek = data_kegiatan.head
                    valid = False
                    
                    while cek:
                        if kegiatan.lower() == cek.nama.lower():
                            valid = True
                            break
                        cek = cek.next
                    if valid:
                        print(f"- {kegiatan}")
        print()
        nomor += 1

while True:
    print("=======================================")
    print(" SISTEM MONITORING KEGIATAN BEM")
    print("=======================================")
    print("1. Tampilkan Data Kegiatan")
    print("2. Cari Kegiatan Berdasarkan Nama")
    print("3. Cari Kegiatan Berdasarkan Tanggal")
    print("4. Tambah Kegiatan Baru")
    print("5. Tampilkan Data Mahasiswa")
    print("6. Cari Mahasiswa Berdasarkan NIM")
    print("7. Tambah Mahasiswa Baru")
    print("8. Tambah Peserta Kegiatan")
    print("9. Tampilkan Data Evaluasi")
    print("10. Statistik")
    print("11. Keluar")

    pilihan = input("\nMasukkan pilihan : ")
    if pilihan == "1":
        data_kegiatan.tampilkan_kegiatan()
    elif pilihan == "2":
        nama = input("Masukkan nama kegiatan : ").strip()
        data_kegiatan.cari_nama(nama)    
    elif pilihan == "3":
        tanggal = input("Masukkan tanggal : ").strip()
        data_kegiatan.cari_tanggal(tanggal)   
    elif pilihan == "4":
        tambah_kegiatan_baru()    
    elif pilihan == "5":
        data_mahasiswa.tampilkan_semua()    
    elif pilihan == "6":
        nim = input("Masukkan NIM : ").strip()
        data_mahasiswa.cari_mahasiswa(nim)   
    elif pilihan == "7":
        tambah_mahasiswa_baru()   
    elif pilihan == "8":
        tambah_peserta()  
    elif pilihan == "9":
        data_evaluasi.tampilkan()
    elif pilihan == "10":
        statistik() 
    elif pilihan == "11":
        print("\nProgram selesai...")
        break
    else:
        print("\nsilahkan pilih nomor yang tersedia!")
        print ()