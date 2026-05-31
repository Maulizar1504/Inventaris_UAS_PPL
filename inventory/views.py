from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Barang, Kategori, Supplier
from .forms import BarangForm, KategoriForm, SupplierForm


# ==========================================
# PUBLIC
# ==========================================

def home(request):

    barang_terbaru = Barang.objects.filter(tampil_di_home=True).order_by('-id')[:6]

    total_barang = Barang.objects.count()

    total_kategori = Kategori.objects.count()

    total_supplier = Supplier.objects.count()

    context = {

        'barang_terbaru': barang_terbaru,

        'total_barang': total_barang,

        'total_kategori': total_kategori,

        'total_supplier': total_supplier,

    }

    return render(
        request,
        'public/home.html',
        context
    )


def about(request):

    return render(
        request,
        'public/about.html'
    )


# ==========================================
# AUTH
# ==========================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            messages.error(
                request,
                'Username atau password salah'
            )

    return render(
        request,
        'auth/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('home')


# ==========================================
# DASHBOARD ADMIN
# ==========================================

@login_required
def dashboard(request):

    total_barang = Barang.objects.count()

    total_kategori = Kategori.objects.count()

    total_supplier = Supplier.objects.count()

    barang = Barang.objects.all().order_by('-id')[:5]

    context = {

        'total_barang': total_barang,

        'total_kategori': total_kategori,

        'total_supplier': total_supplier,

        'barang': barang,

    }

    return render(
        request,
        'dashboard/index.html',
        context
    )


# ==========================================
# CRUD BARANG
# ==========================================

@login_required
def barang_list(request):

    query = request.GET.get('q')

    barang = Barang.objects.all().order_by('-id')

    if query:
        barang = barang.filter(nama__icontains=query)

    context = {

        'barang': barang

    }

    return render(
        request,
        'dashboard/barang/list.html',
        context
    )


@login_required
def barang_create(request):

    form = BarangForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Barang berhasil ditambahkan'
        )

        return redirect('barang_list')

    context = {

        'form': form

    }

    return render(
        request,
        'dashboard/barang/form.html',
        context
    )


@login_required
def barang_update(request, pk):

    barang = get_object_or_404(
        Barang,
        pk=pk
    )

    form = BarangForm(
        request.POST or None,
        request.FILES or None,
        instance=barang
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Barang berhasil diupdate'
        )

        return redirect('barang_list')

    context = {

        'form': form

    }

    return render(
        request,
        'dashboard/barang/form.html',
        context
    )


@login_required
def barang_delete(request, pk):

    barang = get_object_or_404(
        Barang,
        pk=pk
    )

    barang.delete()

    messages.success(
        request,
        'Barang berhasil dihapus'
    )

    return redirect('barang_list')


# ==========================================
# CRUD KATEGORI
# ==========================================

@login_required
def kategori_list(request):

    kategori = Kategori.objects.all()

    context = {

        'kategori': kategori

    }

    return render(
        request,
        'dashboard/kategori/list.html',
        context
    )


@login_required
def kategori_create(request):

    form = KategoriForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('kategori_list')

    return render(
        request,
        'dashboard/kategori/form.html',
        {

            'form': form

        }
    )


@login_required
def kategori_update(request, pk):

    kategori = get_object_or_404(
        Kategori,
        pk=pk
    )

    form = KategoriForm(
        request.POST or None,
        instance=kategori
    )

    if form.is_valid():

        form.save()

        return redirect('kategori_list')

    return render(
        request,
        'dashboard/kategori/form.html',
        {

            'form': form

        }
    )


@login_required
def kategori_delete(request, pk):

    kategori = get_object_or_404(
        Kategori,
        pk=pk
    )

    kategori.delete()

    return redirect('kategori_list')


# ==========================================
# CRUD SUPPLIER
# ==========================================

@login_required
def supplier_list(request):

    supplier = Supplier.objects.all()

    return render(
        request,
        'dashboard/supplier/list.html',
        {

            'supplier': supplier

        }
    )


@login_required
def supplier_create(request):

    form = SupplierForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('supplier_list')

    return render(
        request,
        'dashboard/supplier/form.html',
        {

            'form': form

        }
    )


@login_required
def supplier_update(request, pk):

    supplier = get_object_or_404(
        Supplier,
        pk=pk
    )

    form = SupplierForm(
        request.POST or None,
        instance=supplier
    )

    if form.is_valid():

        form.save()

        return redirect('supplier_list')

    return render(
        request,
        'dashboard/supplier/form.html',
        {

            'form': form

        }
    )


@login_required
def supplier_delete(request, pk):

    supplier = get_object_or_404(
        Supplier,
        pk=pk
    )

    supplier.delete()

    return redirect('supplier_list')