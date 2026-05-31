from django.contrib import admin
from django.utils.html import format_html

from .models import Barang, Kategori, Supplier


@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nama',
        'created_at',
    )

    search_fields = (
        'nama',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nama',
        'telepon',
        'created_at',
    )

    search_fields = (
        'nama',
        'telepon',
    )


@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'kode_barang',
        'nama',
        'kategori',
        'supplier',
        'stok',
        'lokasi',
        'status',
        'preview',
    )

    list_filter = (
        'kategori',
        'supplier',
        'status',
    )

    search_fields = (
        'kode_barang',
        'nama',
        'lokasi',
    )

    list_per_page = 10

    def preview(self, obj):

        if obj.gambar:

            return format_html(
                '<img src="{}" width="70" style="border-radius:10px;" />',
                obj.gambar.url
            )

        return "No Image"

    preview.short_description = "Preview"