from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Khoi)
admin.site.register(Khoa)
admin.site.register(Nhan_vien)
admin.site.register(Quy_trinh)
admin.site.register(Buoc_quy_trinh)
admin.site.register(Quy_trinh_giam_sat)

