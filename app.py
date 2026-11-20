# ==========================================
# PROGRAM APLIKASI LAUNDRY 
# ==========================================

# ==========================================
# BAGIAN 1: Input Data Pelanggan
# ==========================================

print("=" * 40)
print("       SELAMAT DATANG DI LAUNDRY")
print("=" * 40)

nama = str(input("Masukkan Nama          : "))
no_telp = str(input("Masukkan No Telepon    : "))
alamat = str(input("Masukkan Alamat        : "))

print("-" * 40)



# ==========================================
# BAGIAN 2: Pilihan Layanan, Input Berat, & Subtotal
# ==========================================

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




# ==========================================
# BAGIAN 3: Pengecekan Diskon & Pilihan Delivery 
# ==========================================

# mengecek apakah subtotal bernilai lebih dari 0 (artinya pilihan jasa sebelumnya valid)
if subtotal > 0:
    print("-" * 40)
    
    if subtotal >= 150000:
        diskon = subtotal * 20/100
        persen_diskon = "20%"
    elif subtotal >= 100000:
        diskon = subtotal * 15/100
        persen_diskon = "15%"
    elif subtotal >= 50000:
        diskon = subtotal * 10/100
        persen_diskon = "10%"
    else:
        diskon = 0
        persen_diskon = "0%"

    # Tampilkan pesan jika mendapatkan diskon > 0%
    if diskon > 0:
        print("~" * 40)
        print(f"🎉 HOREE! ANDA MENDAPATKAN DISKON {persen_diskon}!")
        print(f"   Potongan Harga : Rp {diskon:,.0f}")
        print("~" * 40)
    else:
        print("[i] Belanja minimal Rp 50.000 untuk mendapatkan diskon menarik!")

    # Hitung total setelah diskon
    total_setelah_diskon = subtotal - diskon

    print("-" * 40)
    print("📦 PILIHAN OPSI DELIVERY:")
    print("   1. Diantar ke rumah (Ongkir Rp 10.000)")
    print("   2. Ambil sendiri (Tanpa Ongkir)")
    print("-" * 40)

    # Input pilihan delivery
    pilihan_delivery = int(input("Masukkan pilihan delivery (1/2): "))

    # 2. Logika Pengecekan Delivery & Ongkir
    if pilihan_delivery == 1:
        biaya_delivery = 10000
        keterangan_delivery = "Diantar ke rumah"
    elif pilihan_delivery == 2:
        biaya_delivery = 0
        keterangan_delivery = "Ambil sendiri"
    else:
        biaya_delivery = 0
        keterangan_delivery = "Pilihan delivery tidak tersedia"
        print("[!] Mohon maaf, pilihan delivery salah.")

    # Hitung total pembayaran akhir (Total setelah diskon + ongkir)
    total_pembayaran_akhir = total_setelah_diskon + biaya_delivery

else:
    # Jika dari awal jasa tidak tersedia, set semua nilai jadi 0
    diskon = 0
    persen_diskon = "0%"
    total_setelah_diskon = 0
    biaya_delivery = 0
    keterangan_delivery = "-"
    total_pembayaran_akhir = 0
    print("[!] Transaksi dibatalkan karena pilihan jasa tidak valid.")



# ==========================================
# BAGIAN 4: CETAK STRUK PEMBAYARAN 
# ==========================================

print("\n")
print("\n*・。.・゜✭・.・✫・゜・。.・*・。.・゜✭・*")
print("           🫧  STRUK LAUNDRY 🫧             ")
print("*・。.・゜✭・.・✫・゜・。.・*・。.・゜✭・*")
print("Nama Pelanggan :", nama)
print("No. Telepon    :", no_telp)
print("Alamat         :", alamat)
print("Jenis Jasa     :", jenis_jasa)
print("Berat Pakaian  :", berat, "Kg")
print("Harga per Kg   : Rp", format(tarif, ","))
print("┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄")
print("Subtotal       : Rp", format(subtotal, ","))
print("Diskon         :", persen_diskon)
print("Potongan Harga : Rp", format(diskon, ","))
print("Delivery       :", keterangan_delivery)
print("Biaya Delivery : Rp", format(biaya_delivery, ","))
print("══════════════════════════════════════════")
print("TOTAL BAYAR    : Rp", format(total_pembayaran_akhir, ","))
print("══════════════════════════════════════════")
print("               TERIMA KASIH            ")
print("             ATAS PESANAN ANDA         ")
print("*・。.・゜✭・.・✫・゜・。.・*・。.・゜✭・*")
print("\n")