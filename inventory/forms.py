from django import forms

from .models import (
    Barang,
    Kategori,
    Supplier
)

from .models import BorrowRequest


class BarangForm(forms.ModelForm):

    class Meta:

        model = Barang

        fields = '__all__'

        widgets = {

            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'kategori': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'supplier': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'stok': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'lokasi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'gambar': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


class KategoriForm(forms.ModelForm):

    class Meta:

        model = Kategori

        fields = '__all__'

        widgets = {

            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }


class SupplierForm(forms.ModelForm):

    class Meta:

        model = Supplier

        fields = '__all__'

        widgets = {

            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'alamat': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'telepon': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }



class BorrowRequestForm(forms.ModelForm):

    class Meta:
        model = BorrowRequest
        fields = (
            'nama', 'nim', 'email', 'telepon', 'barang', 'alasan', 'surat'
        )

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'barang': forms.Select(attrs={'class': 'form-select'}),
            'alasan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'surat': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }