from Giam_sat_quy_trinh.views import *
from django.urls import path, include
from Nhan_vien.views import*

app_name = 'Nhan_vien'
urlpatterns = [
    path('tai-khoan-cua-toi',taikhoancuatoi, name ='taikhoancuatoi'),
    path('dang-xuat',dang_xuat,name='dang_xuat'),
    path('dang-nhap/',dang_nhap,name='dang_nhap'),
]