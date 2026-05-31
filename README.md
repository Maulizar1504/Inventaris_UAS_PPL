# SmartInventory

SmartInventory adalah aplikasi web inventaris barang berbasis Django yang dibuat untuk memenuhi tugas Final Stage mata kuliah Proyek Perangkat Lunak.

---

# Fitur Aplikasi

## Public Page

* Landing Page
* About Page
* Informasi Inventaris

## Admin Dashboard

* Login Admin
* Dashboard Statistik
* CRUD Barang
* CRUD Kategori
* CRUD Supplier
* Upload Foto Barang
* Search Barang
* Pagination
* Export PDF

---

# Teknologi

* Python
* Django
* Bootstrap 5
* SQLite
* Chart.js
* ReportLab

---

# Struktur Project

```bash
smartinventory/
│
├── inventory/
├── media/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# Cara Instalasi

## 1. Clone Repository

```bash
git clone <link-repository>
```

---

## 2. Masuk Folder Project

```bash
cd 2308107010007_UAS
```

---

## 3. Buat Virtual Environment

```bash
python -m venv venv
```

---

## 4. Aktifkan Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

---

## 5. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 6. Jalankan Migrasi Database

```bash
python manage.py migrate
```

---

## 7. Buat Admin

```bash
python manage.py createsuperuser
```

---

## 8. Jalankan Server

```bash
python manage.py runserver
```

---

# Akses Aplikasi

## Landing Page

```text
http://127.0.0.1:8000/
```

## Login Admin

```text
http://127.0.0.1:8000/login/
```

## Dashboard Admin

```text
http://127.0.0.1:8000/dashboard/
```

---

# Akun Admin

Gunakan akun admin yang dibuat melalui:

```bash
python manage.py createsuperuser
```

---

# Ketentuan Keamanan

* Dashboard hanya dapat diakses oleh admin yang login.
* Halaman public dapat diakses tanpa login.
* Semua fitur CRUD diproteksi login authentication Django.

---

# Dibuat Untuk

Final Stage — Proyek Perangkat Lunak 2026