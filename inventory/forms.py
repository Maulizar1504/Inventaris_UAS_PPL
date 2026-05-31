from django import forms

from .models import (
    Barang,
    Kategori,
    Supplier
)


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