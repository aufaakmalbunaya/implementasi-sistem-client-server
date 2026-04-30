# IMPLEMENTASI SISTEM CLIENT–SERVER

> Proyek Akhir — Sistem Client–Server berbasis TCP Socket dengan Python.

## Identitas Proyek

- **Judul:** IMPLEMENTASI SISTEM CLIENT–SERVER
- **Project Manager:** Nawal Arifah
- **Kelompok:** Kelompok 5
- **Akun GitHub:** [`aufaakmalbunaya`](https://github.com/aufaakmalbunaya)
- **Repository:** [https://github.com/aufaakmalbunaya/implementasi-sistem-client-server](https://github.com/aufaakmalbunaya/implementasi-sistem-client-server)

## Deskripsi Proyek

Proyek ini mengimplementasikan **sistem client–server berbasis TCP** menggunakan
bahasa Python. Server berperan sebagai penyedia layanan kuis aritmatika,
sedangkan client berperan sebagai pengguna yang menjawab soal.

Server akan:
1. Membuat TCP socket.
2. Bind ke `10.6.6.41:5020`.
3. Listen koneksi dari client.
4. Menerima koneksi client.
5. Mengirim *welcome message* dan soal aritmatika acak.
6. Menerima jawaban client.
7. Memvalidasi jawaban.
8. Mengirim respons `BENAR`, `SALAH. Jawaban benar: ...`, atau `Input tidak valid`.
9. Kembali ke mode listen untuk client lain.

Komunikasi menggunakan **string ber-encoding UTF-8** dan mengikuti pola
**request–response** di atas TCP, dengan delimiter newline (`\n`).

## Arsitektur Sistem

```
+---------+        TCP/5020        +---------+
| Client  |  <------------------>  | Server  |
| (Py)    |   request / response   | (Py)    |
+---------+                        +---------+
```

## Fitur Server

- Listen di `0.0.0.0:5020`.
- Multi-client menggunakan **threading**.
- Generator soal aritmatika (`+`, `-`, `*`).
- Validasi jawaban (integer / non-integer / `exit`).
- Logging aktivitas ke `logs/server.log`.
- Graceful shutdown via `Ctrl+C`.

## Fitur Client

- Connect ke `HOST:5020`.
- Menerima welcome + soal dari server.
- Mengirim jawaban via `input()`.
- Menerima dan menampilkan respons server.
- Mendukung perintah `exit` untuk keluar.
- Penutupan koneksi yang aman.

## Alur Komunikasi

1. Server start → listen di port 5020.
2. Client connect → server kirim welcome + soal.
3. Client kirim jawaban (string + `\n`).
4. Server balas: `BENAR`, `SALAH. Jawaban benar: X`, atau `Input tidak valid`.
5. Server kirim soal berikutnya — loop sampai client mengirim `exit`.

## Struktur Folder

```
implementasi-sistem-client-server/
├── README.md
├── .gitignore
├── src/
│   ├── server.py
│   └── client.py
├── docs/
│   └── Client-and-server_Kelompok 5.pdf
├── screenshots/
│   └── execution-screenshot.png
└── logs/
    └── server.log
```

## Requirements

- **Python 3.10+**
- **Sistem Operasi:** Windows / Linux / macOS
- **Library:** hanya library standar Python (`socket`, `threading`, `random`, `logging`).

> Tidak perlu `pip install` apa-apa.

## Cara Menjalankan di Windows

### 1. Jalankan Server

Buka **Git Bash / CMD / PowerShell**, lalu:

```bash
cd implementasi-sistem-client-server
python src/server.py
```

Output yang diharapkan:

```
[2025-xx-xx ...] Server berjalan di 0.0.0.0:5020
Menunggu koneksi client...
```

### 2. Jalankan Client

Buka **terminal kedua**:

```bash
cd implementasi-sistem-client-server
python src/client.py
```

> Jika client dan server berada di **perangkat yang berbeda**, ubah `HOST`
> di `src/client.py` menjadi IP server. Cari IP server dengan `ipconfig`
> (Windows) — gunakan `IPv4 Address` dari adapter aktif.

## Contoh Output

**Sisi Client:**
```
Terhubung ke server 127.0.0.1:5020
Selamat datang di Kuis Aritmatika!
Ketik 'exit' untuk keluar.
SOAL: Berapa hasil dari 7 + 5 ?
Jawaban Anda: 12
Server: BENAR

SOAL: Berapa hasil dari 9 * 3 ?
Jawaban Anda: 20
Server: SALAH. Jawaban benar: 27

SOAL: Berapa hasil dari 4 - 2 ?
Jawaban Anda: dua
Server: Input tidak valid
```

## Kemungkinan Error & Solusi

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `ConnectionRefusedError` | Server belum dijalankan / port salah | Jalankan `server.py` dulu, cek port 5020 |
| `OSError: [WinError 10048]` | Port 5020 dipakai aplikasi lain | Tutup aplikasi lain atau ubah `PORT` di kedua file |
| `ModuleNotFoundError` | Python tidak terinstall benar | Reinstall Python, centang `Add to PATH` |
| Firewall memblokir koneksi | Windows Defender Firewall | Allow Python di firewall saat prompt muncul |

## Pengembangan Lanjutan

- Multi-client via threading (✓ sudah).
- Logging ke `server.log` (✓ sudah).
- Newline-based protocol (✓ sudah).
- Tambahan ide: skor pemain, level kesulitan, GUI client (Tkinter).

## Riwayat Commit

Repository ini memiliki **minimal 3 commit** dengan pesan deskriptif:
1. `Initial commit: add README and gitignore`
2. `Add TCP client-server quiz implementation`
3. `Add project documentation and execution screenshots`

## Lisensi / Catatan Akademik

Proyek ini dibuat untuk memenuhi tugas mata kuliah **Kapita Selekta Sistem Komputer dan Jaringan**. Tidak untuk kepentingan komersial.
