class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def status(self):
        return "LULUS" if self.nilai >= 75 else "TIDAK LULUS"

    def __str__(self):
        return(f"Nama : {self.nama} ({self.nilai}) → {self.status()}")
    
    def tampil(self):
        return(f"Nama : {self.nama} ({self.nilai})")
    
    def to_d(self):
        return {
            "nama" : self.nama,
            "nilai" : self.nilai
        }
    @classmethod
    def cari_siswa(cls, data, nama):
        for s in data:
            if s.nama.lower() == nama.lower():
                return s
        return None
        
    @classmethod
    def rata(cls, data):
        if len(data) == 0:
            return 0
        total = sum(s.nilai for s in data)
        return total/len(data)
    
    @classmethod
    def rank(cls, data, reverse=True):
        return sorted(data, key=lambda s: s.nilai, reverse=reverse)
    
    @classmethod
    def filter(cls, data, status):
        return[s for s in data if s.status() == status]