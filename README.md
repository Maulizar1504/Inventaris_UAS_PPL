📦 SmartInventory
SmartInventory adalah aplikasi web manajemen inventaris barang berbasis Django yang dikembangkan untuk memenuhi tugas Final Stage mata kuliah Proyek Perangkat Lunak (2026). Aplikasi ini digunakan untuk mengelola data barang, kategori, supplier, serta proses peminjaman barang dengan sistem admin dashboard yang terproteksi.

✨ Fitur Utama
- Public Page
- Landing Page
- About Page
- Informasi Inventaris Barang
- Form Permintaan Peminjaman Barang

🛠️ Admin Dashboard
- Login Admin (Authentication)
- Dashboard Statistik (Chart.js)
- CRUD Barang
- CRUD Kategori
- CRUD Supplier
- Upload & manajemen foto barang
- Search & Pagination
- Export PDF (ReportLab)
- Manajemen permintaan peminjaman barang

🧰 Teknologi yang Digunakan
- Python 3.x
- Django
- Bootstrap 5
- SQLite
- Chart.js
- ReportLab

📁 Struktur Project
smartinventory/
│
├── inventory/            # App utama
├── media/                # File upload (gambar & dokumen)
├── smartinventory/       # Config project Django
├── templates/            # HTML templates
├── static/               # CSS, JS, images, favicon
├── db.sqlite3            # Database SQLite
├── manage.py
├── requirements.txt
└── README.md

🚀 Cara Instalasi & Menjalankan Project
1. Clone Repository
git clone <link-repository>
2. Masuk ke Folder Project
cd 2308107010007_UAS
3. Buat Virtual Environment
python -m venv venv
4. Aktifkan Virtual Environment
Windows:venv\Scripts\activate
5. Install Dependency
pip install -r requirements.txt
6. Migrasi Database
python manage.py migrate
7. Buat Admin User
python manage.py createsuperuser
8. Jalankan Server
python manage.py runserver

🌍 Akses Aplikasi
🏠 Landing Page
http://127.0.0.1:8000/
🔐 Login Admin
http://127.0.0.1:8000/login/
📊 Dashboard Admin
http://127.0.0.1:8000/dashboard/

🔐 Sistem Keamanan
Dashboard hanya dapat diakses oleh admin yang sudah login
Semua fitur CRUD dilindungi oleh Django Authentication
Halaman public dapat diakses tanpa login
Upload file dan media hanya melalui sistem backend

📂 Data Media
Project ini sudah mendukung:
- Upload gambar barang
- Upload dokumen peminjaman
- Penyimpanan otomatis di folder media/
- Fitur Tambahan
- Pagination data barang
- Pencarian barang
- Statistik dashboard dengan grafik
- Export laporan dalam format PDF
- Manajemen peminjaman barang

🎯 Tujuan Project
Project ini dibuat untuk:
Final Stage — Proyek Perangkat Lunak 2026
Sebagai implementasi sistem informasi inventaris berbasis web menggunakan Django.