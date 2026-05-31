from django.urls import path
from . import views


urlpatterns = [

    # =========================================
    # PUBLIC
    # =========================================

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'borrow/',
        views.borrow_request,
        name='borrow_request'
    ),


    # =========================================
    # AUTH
    # =========================================

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),


    # =========================================
    # DASHBOARD
    # =========================================

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # =========================================
    # CRUD BARANG
    # =========================================

    path(
        'dashboard/barang/',
        views.barang_list,
        name='barang_list'
    ),

    path(
        'dashboard/barang/tambah/',
        views.barang_create,
        name='barang_create'
    ),

    path(
        'dashboard/barang/export/pdf/',
        views.barang_export_pdf,
        name='barang_export_pdf'
    ),

    path(
        'dashboard/barang/edit/<int:pk>/',
        views.barang_update,
        name='barang_update'
    ),

    path(
        'dashboard/barang/delete/<int:pk>/',
        views.barang_delete,
        name='barang_delete'
    ),


    # =========================================
    # CRUD KATEGORI
    # =========================================

    path(
        'dashboard/kategori/',
        views.kategori_list,
        name='kategori_list'
    ),

    path(
        'dashboard/kategori/tambah/',
        views.kategori_create,
        name='kategori_create'
    ),

    path(
        'dashboard/kategori/edit/<int:pk>/',
        views.kategori_update,
        name='kategori_update'
    ),

    path(
        'dashboard/kategori/delete/<int:pk>/',
        views.kategori_delete,
        name='kategori_delete'
    ),


    # =========================================
    # CRUD SUPPLIER
    # =========================================

    path(
        'dashboard/supplier/',
        views.supplier_list,
        name='supplier_list'
    ),

    path(
        'dashboard/supplier/tambah/',
        views.supplier_create,
        name='supplier_create'
    ),

    path(
        'dashboard/supplier/edit/<int:pk>/',
        views.supplier_update,
        name='supplier_update'
    ),

    path(
        'dashboard/supplier/delete/<int:pk>/',
        views.supplier_delete,
        name='supplier_delete'
    ),

]