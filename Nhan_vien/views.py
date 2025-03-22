from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from Giam_sat_quy_trinh.models import *
from Nhan_vien.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from App_nhan_vien.forms import FormRegister
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import os
from django.conf import settings
import pdfkit
from django.utils import timezone
# Create your views here.

def taikhoancuatoi(request):
    return render(request, 'Nhan_vien/taikhoancuatoi.html')

def dang_nhap(request):
    if 's_nhan_vien' in request.session:
        return redirect('Giam_sat_quy_trinh:trang_chu')
    else:
        result=""
        if request.POST.get('Ma_nhan_vien'):
            # hasher = PBKDF2PasswordHasher()
            #mk=hasher.encode(request.POST.get('password'),'qhf')
            ma_nv=request.POST.get('Ma_nhan_vien')
            mk= request.POST.get('mat_khau')
            nguoidung= Nhan_vien.objects.filter(ma_nhan_vien=ma_nv, mat_khau=mk)
            if nguoidung.count()>0:
                dict_nhan_vien = nguoidung.values()[0]
                request.session['s_nhan_vien'] = dict_nhan_vien #bước này là tạo session với tên là s_nhan_vien
                return redirect('Giam_sat_quy_trinh:trang_chu')
            else:
                result='''<div class="alert alert-danger" role="alert" class="center-block">
                                            Đăng nhập thất bại. Xin thử lại.
                                        </div>'''
                return render (request, 'Nhan_vien/dangnhap.html',{
                    'result':result,
                })
        return render (request, 'Nhan_vien/dangnhap.html',{
            'result':result,
        })

def dang_xuat(request):
    if 's_nhan_vien' in request.session:
        del request.session['s_nhan_vien']
    return redirect('Nhan_vien:dang_nhap')