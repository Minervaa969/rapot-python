def login():
    akun = {
        "guru":{
            "password": "guru123",
            "role" : "guru"
        },
        "siswa":{
            "password": "siswa123",
            "role" : "siswa"
        }
    }
    while True:
        print("\n===== LOGIN =====")
        username = input("username : ")
        password = input("password : ")

        if username in akun and akun[username]["password"] == password:
            print(f"Login berhasil! Selamat datang, {username}!")
            print(f"Role Anda: {akun[username]['role']}")
            return akun[username]['role']
        else:
            print("Login gagal! Pastikan username dan password benar.")