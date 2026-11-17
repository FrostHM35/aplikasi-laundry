# 🧺 Project Aplikasi Laundry Terminal (Python)

Project sederhana pengelolaan manajemen laundry berbasis terminal menggunakan bahasa pemrograman Python. Project ini dibuat sebagai tugas kelompok mata kuliah pemrograman.

---

## 👥 Anggota Kelompok & Pembagian Tugas

Project ini dikerjakan secara kolaboratif menggunakan Git & GitHub dengan pembagian tugas sebagai berikut:

| No | Nama Anggota | Bagian / Modul yang Dikerjakan |
| :--- | :--- | :--- |
| 1. | **Anggota 1** | Inisialisasi program, Judul, & Input Data Pelanggan (Nama, No Telp, Alamat, Email) |
| 2. | **Anggota 2** | Menu Pilihan Jenis Jasa (Cuci Kering, Setrika, Express), Input Berat (Kg), & Perhitungan Subtotal |
| 3. | **Anggota 3** | Logika Pengecekan Diskon Bertingkat (`>=` 100rb, 150rb, 200rb) & Opsi Pilihan Delivery/Ongkir |
| 4. | **Anggota 4** | Perhitungan Total Pembayaran Akhir & Desain Cetak Struk / Output di Terminal |

---

## 📋 Fitur Utama Aplikasi
1. **Input Data Konsumen:** Merekam data diri pelanggan secara interaktif.
2. **Pilihan Layanan Fleksibel:** 
   * Cuci Kering (Rp 5.000 / kg)
   * Cuci Setrika (Rp 7.000 / kg)
   * Cuci Express (Rp 10.000 / kg)
3. **Sistem Diskon Otomatis (Minimal Subtotal):**
   * Belanja $\ge$ Rp 200.000 $\rightarrow$ Diskon 20%
   * Belanja $\ge$ Rp 150.000 $\rightarrow$ Diskon 15%
   * Belanja $\ge$ Rp 100.000 $\rightarrow$ Diskon 10%
4. **Opsi Pengiriman (Delivery):** Layanan antar ke rumah (ongkir Rp 10.000) atau ambil sendiri (tanpa ongkir).
5. **Struk Otomatis:** Menampilkan rincian transaksi secara lengkap di terminal.

---

## ⚙️ Cara Menjalankan Program

Pastikan komputer Anda sudah terinstal Python. Jalankan langkah-langkah berikut di terminal atau command prompt:

1. Clone repository ini ke komputer lokal Anda:
   ```bash
   git clone https://github.com/FrostHM35/aplikasi-laundry.git