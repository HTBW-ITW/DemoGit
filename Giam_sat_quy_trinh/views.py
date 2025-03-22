from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from Nhan_vien.models import *
from Giam_sat_quy_trinh.models import *
import os
import pdfkit
from django.conf import settings

# Create your views here.
def trang_chu(request):
    if not 's_nhan_vien' in request.session:
        return redirect('Nhan_vien:dang_nhap')
    else:
        return render(request, 'Giam_sat_quy_trinh/index.html')

def master(request):
    if not 's_nhan_vien' in request.session:
        return render(request, 'Giam_sat_quy_trinh/master.html',{
        })
    else:
        nv_dang_nhap = request.session['s_nhan_vien']
        return render(request, 'Giam_sat_quy_trinh/master.html',{
            'nv_dang_nhap':nv_dang_nhap,
        })

def giam_sat_quy_trinh(request):
    if not 's_nhan_vien' in request.session:
        return redirect('Nhan_vien:dang_nhap')
    else:
        ds_quy_trinh = Quy_trinh.objects.all()
        paginator = Paginator(ds_quy_trinh, 10) # Show 5 quy trình mỗi page
        page_number = request.GET.get("trang")
        try:
            page_quy_trinh = paginator.page(page_number)
        except PageNotAnInteger:
            # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
            page_quy_trinh = paginator.page(1)
        except EmptyPage:
            # Nếu page không có item nào, trả về page cuối cùng
            page_quy_trinh = paginator.page(paginator.num_pages)
        return render(request, 'Giam_sat_quy_trinh/giamsatquytrinh.html',{
            'ds_quy_trinh':ds_quy_trinh,
            'page_quy_trinh':page_quy_trinh,
        })

def form_quy_trinh(request,id_Ten_quy_trinh):
    if not 's_nhan_vien' in request.session:
        return redirect('Nhan_vien:dang_nhap')
    else:
        ds_nhan_vien = Nhan_vien.objects.all()
        idquytrinh = id_Ten_quy_trinh
        a = Buoc_quy_trinh.objects.filter(Ten_quy_trinh_id=id_Ten_quy_trinh)
        tenquytrinh = a.values()[0]['Ten_quy_trinh_id']
        ds_quy_trinh = Quy_trinh.objects.filter(id=id_Ten_quy_trinh)
        sobuoc_string = ds_quy_trinh.values()[0]['So_buoc']
        sobuoc_int = int(sobuoc_string)
        if request.POST.get('B01'):
            nv_giam_sat = request.session['s_nhan_vien']
            id_nv_duoc_giam_sat = request.POST.get('NV_duoc_gs')
            kq_list = []
            for i in range (0,sobuoc_int):
                tenbuoc = str(a.values()[i]['Ma_buoc_QT'])
                kq_temporary = request.POST.get(tenbuoc)
                kq_temporary2 ="#" + tenbuoc + "|" + kq_temporary
                kq_list.append(kq_temporary2)
            kq =''
            for s in kq_list:
                kq = kq + s
            print(nv_giam_sat['ma_nhan_vien'], type(nv_giam_sat['ma_nhan_vien']))
            phieu_giam_sat = Quy_trinh_giam_sat.objects.create(
                        Nhan_vien_giam_sat_id=nv_giam_sat['id'],
                        ID_Nhan_vien_duoc_giam_sat=id_nv_duoc_giam_sat,
                        Ten_quy_trinh_id=id_Ten_quy_trinh,
                        Kq_gs=kq)
        return render(request, 'Giam_sat_quy_trinh/formquytrinh.html',{
            'tenquytrinh':tenquytrinh,
            'a':a,
            'ds_nhan_vien':ds_nhan_vien,
        })


