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