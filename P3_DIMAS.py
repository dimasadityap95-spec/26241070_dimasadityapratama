# P3_26241070_Dimas.py
# Program Identitas Mahasiswa

print("=" * 32)
print("     IDENTITAS MAHASISWA")
print()

# Input data (semua memakai input())
nama = input("Masukkan Nama           : ")
nim = int(input("Masukkan NIM            : "))
prodi = input("Masukkan Program Studi  : ")
dua_digit_nim = int(input("Masukkan 2 Digit Akhir NIM : "))

# Tampilkan hasil
print()
print("=" * 32)
print("        HASIL PROGRAM")
print("=" * 32)
print()
print("Nama          :", nama)
print("NIM           :", nim)
print("Prodi         :", prodi)
print("2 Digit NIM   :", dua_digit_nim)
print()
print("Tipe Data Nama:", type(nama))
print("Tipe Data NIM :", type(nim))
print("Tipe Data Prodi :", type(prodi))
print("Tipe Data 2 Digit NIM :", type(dua_digit_nim))
print("=" * 32)