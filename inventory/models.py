from django.db import models
from datetime import datetime

# ==========================================
# KATEGORI
# ==========================================

class Kategori(models.Model):

    nama = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nama


# ==========================================
# SUPPLIER
# ==========================================

class Supplier(models.Model):

    nama = models.CharField(
        max_length=100
    )

    alamat = models.TextField()

    telepon = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nama


# ==========================================
# BARANG
# ==========================================

class Barang(models.Model):

    STATUS_CHOICES = (

        ('Tersedia', 'Tersedia'),
        ('Dipinjam', 'Dipinjam'),
        ('Rusak', 'Rusak'),

    )

    kode_barang = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    nama = models.CharField(
        max_length=200
    )

    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    stok = models.IntegerField()

    lokasi = models.CharField(
        max_length=200
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Tersedia'
    )

    gambar = models.ImageField(
        upload_to='barang/',
        blank=True,
        null=True
    )

    tampil_di_home = models.BooleanField(
        default=True,
        help_text='Tampilkan barang ini di halaman utama (landing page)'
    )

    featured = models.BooleanField(
        default=False,
        help_text='Tandai sebagai featured untuk prioritas tampilan di landing page'
    )

    deskripsi = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.kode_barang:

            tahun = datetime.now().year

            last_id = Barang.objects.count() + 1

            self.kode_barang = (
                f"INF-{tahun}-{last_id:03d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.kode_barang} - {self.nama}"



# ==========================================
# REQUESTS / PEMINJAMAN
# ==========================================


class BorrowRequest(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    nama = models.CharField(max_length=200)

    nim = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField()

    telepon = models.CharField(max_length=20, blank=True, null=True)

    barang = models.ForeignKey(
        Barang,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    alasan = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.nama} - {self.barang or 'Generic request'}"

    surat = models.FileField(
        upload_to='surat/',
        blank=True,
        null=True,
        help_text='Unggah surat permohonan/pengantar (PDF/JPG/PNG)'
    )