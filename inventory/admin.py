from django.contrib import admin
from django.utils.html import format_html

from .models import Barang, Kategori, Supplier
from .models import BorrowRequest


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
        'tampil_di_home',
        'featured',
        'preview',
    )

    list_filter = (
        'kategori',
        'supplier',
        'status',
        'tampil_di_home',
        'featured',
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


@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'nama', 'nim', 'email', 'telepon', 'barang', 'status', 'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'nama', 'nim', 'email',
    )
    readonly_fields = ('created_at',)
    fields = ('nama','nim','email','telepon','barang','alasan','surat','status','created_at')