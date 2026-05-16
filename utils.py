import json
from models import Siswa

def validasi(data):
    if not data:
        print("Data Siswa Belum Diinput!")
        return False
    return True

def menu_input(data):
    try:
        jumlah = int(input("Masukan jumlah siswa : "))
        for i in range(jumlah):
            nama = input("\nNama siswa  : ")
            if Siswa.cari_siswa(data, nama):
                print("Data Siswa Sudah Ada!")
                return
            nilai = int(input("Nilai siswa : "))
            data.append(Siswa(nama, nilai))
            save_data(data)
        print("\nData Siswa Berhasil Ditambahkan!")
    except ValueError:
        print("Input Harus Angka!")

def menu_tampil(data):
    if not validasi(data):
        return
    print("===== DAFTAR NILAI KELAS CODING SISWA =====")
    for i, s in enumerate (data, start=1):
        print(f"{i}. {s.tampil()}")

def menu_cari(data):
    if not validasi(data):
        return
    nama = input("Masukan nama siswa : ")
    siswa = Siswa.cari_siswa(data, nama)
    if siswa:
        print("Data Siswa Ditemukan!")
        print(siswa.tampil())
    else:
        print("Data Siswa Tidak Ditemukan!")

def menu_update(data):
    if not validasi(data):
        return
    nama = input("Masukan nama siswa yang akan diupdate : ")
    siswa = Siswa.cari_siswa(data, nama)
    if siswa:
        print(siswa.tampil())
        data_baru = int(input("Masukan Nilai Terbaru Siswa : "))
        siswa.nilai = data_baru
        save_data(data)
        print("Update Berhasil!")
    else:
        print("Data Siswa Tidak Ditemukan!")

def menu_hapus(data):
    if not validasi(data):
        return
    nama = input("Masukan nama siswa yang akan dihapus : ")
    siswa = Siswa.cari_siswa(data, nama)
    if siswa:
        print(siswa.tampil())
        konfir = input("Yakin hapus data siswa ini (y/n) : ")
        if konfir.lower() == "y":
            data.remove(siswa)
            save_data(data)
            print("Data Siswa Berhasil Dihapus!")
        else:
            print("Penghapusan Dibatalkan!")
    else:
        print("Data Siswa Tidak Ditemukan!")

def menu_rank(data, reverse=True):
    if not validasi(data):
        return
    hasil = Siswa.rank(data, reverse)
    print("===== LEADERBOARD NILAI KELAS CODING =====")
    for i, s in enumerate(hasil, start=1):
        print(f"{s.tampil()} [RANKING : {i}]")

def menu_filter(data, status="LULUS"):
    if not validasi(data):
        return
    saring = Siswa.filter(data, status)
    for s in saring:
        print(s)

def menu_rata(data):
    if not validasi(data):
        return
    print(f"Rata-rata Nilai Kelas Coding : {Siswa.rata(data):.2f}")

def save_data(data):
    with open("data_siswa.json", "w") as file:
        json.dump([s.to_d() for s in data], file, indent=4)

def load_data():
    try:
        with open("data_siswa.json", "r") as file:
            data_json = json.load(file)
            return [
                Siswa(s["nama"], s["nilai"])
                for s in data_json
            ]
    except (FileNotFoundError, json.JSONDecodeError):
        return []