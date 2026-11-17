# ==========================================
# PROGRAM APLIKASI LAUNDRY 
# ==========================================

print("=" * 40)
print("       SELAMAT DATANG DI LAUNDRY KITA")
print("=" * 40)

# ==========================================
# BAGIAN 1: Input Data Pelanggan (Anggota 1)
# ==========================================
nama = str(input("Masukkan Nama          : "))
no_telp = str(input("Masukkan No Telepon    : "))
alamat = str(input("Masukkan Alamat        : "))

print("-" * 40)

# === BAGIAN ANGGOTA 2: Pilihan Layanan, Input Berat, & Subtotal ===

print("\n--- PILIHAN JENIS JASA ---")
print("1. Cuci Kering  (Rp 5.000 / kg)")
print("2. Cuci Setrika (Rp 7.000 / kg)")
print("3. Cuci Express (Rp 10.000 / kg)")

# Input pilihan jasa menggunakan nomor (integer)
pilihan = int(input("Masukkan pilihan jenis jasa (1/2/3): "))

# Logika pengecekan berdasarkan nomor pilihan
if pilihan == 1:
    tarif = 5000
    jenis_jasa = "Cuci Kering"
elif pilihan == 2:
    tarif = 7000
    jenis_jasa = "Cuci Setrika"
elif pilihan == 3:
    tarif = 10000
    jenis_jasa = "Cuci Express"
else:
    tarif = 0
    jenis_jasa = "Tidak Tersedia"
    print("[!] Mohon maaf, pilihan jenis jasa tidak tersedia.")

# Jika jasa valid, lanjut ke input berat dan hitung subtotal
if tarif > 0:
    berat = float(input("Masukkan berat cucian (kg): "))
    subtotal = tarif * berat
    print(f"Jenis Jasa : {jenis_jasa}")
    print(f"Subtotal   : Rp {subtotal:,.0f}")
else:
    berat = 0
    subtotal = 0