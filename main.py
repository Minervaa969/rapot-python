from auth import login
from utils import *

data_siswa = load_data()
role = login()

if role == "guru":
    print("Anda memiliki akses penuh sebagai guru.")
    while True:
        print("\n※※※※※  RAPOT KELAS CODING ※※※※※")
        print("1. Input Data Siswa")
        print("2. Daftar Nilai")
        print("3. Cari Siswa")
        print("4. Update Data Siswa")
        print("5. Daftar Siswa Lulus")
        print("6. Daftar Siswa Tidak Lulus")
        print("7. Leaderboard")
        print("8. Rata-rata Nilai Siswa")
        print("9. Hapus Data Siswa")
        print("10. Keluar")
        pilih = input("\nPilih (1-10) : ")

        if pilih == "1":
            menu_input(data_siswa)

        elif pilih == "2":
            menu_tampil(data_siswa)

        elif pilih == "3":
            menu_cari(data_siswa)

        elif pilih == "4":
            menu_update(data_siswa)

        elif pilih == "5":
            print("===== DAFTAR SISWA LULUS =====")
            menu_filter(data_siswa)

        elif pilih == "6":
            print("===== DAFTAR SISWA TIDAK LULUS =====")
            menu_filter(data_siswa, status="TIDAK LULUS")

        elif pilih == "7":
            menu_rank(data_siswa)

        elif pilih == "8":
            menu_rata(data_siswa)

        elif pilih == "9":
            menu_hapus(data_siswa)

        elif pilih == "10":
            print("ANDA TELAH KELUAR DARI SISTEM")
            break

        else:
            print("Input Invalid")

elif role == "siswa":
    print("Anda memiliki akses terbatas sebagai siswa.")
    while True:
        print("\n※※※※※  RAPOT KELAS CODING ※※※※※")
        print("1. Daftar Nilai")
        print("2. Cari Siswa")
        print("3. Rata-rata Nilai Siswa")
        print("4. Leaderboard")
        print("5. Daftar Siswa Lulus")
        print("6. Daftar Siswa Tidak Lulus")
        print("7. Keluar")
        pilih = input("\nPilih (1-7) : ")

        if pilih == "1":
            menu_tampil(data_siswa)

        elif pilih == "2":
            menu_cari(data_siswa)

        elif pilih == "3":
            menu_rata(data_siswa)

        elif pilih == "4":
            menu_rank(data_siswa)

        elif pilih == "5":
            print("===== DAFTAR SISWA LULUS =====")
            menu_filter(data_siswa)

        elif pilih == "6":
            print("===== DAFTAR SISWA TIDAK LULUS =====")
            menu_filter(data_siswa, status="TIDAK LULUS")

        elif pilih == "7":
            print("ANDA TELAH KELUAR DARI SISTEM")
            break

        else:
            print("Input Invalid")

else:
    print("Gagal login. Akses ditolak.")