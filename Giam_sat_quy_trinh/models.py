from django.db import models
from django.utils import timezone
from Nhan_vien.models import *

# Create your models here.

class Quy_trinh(models.Model):
    khoa_QT = models.ForeignKey(Khoa, on_delete=models.PROTECT)
    STT_QT = models.CharField(max_length= 300)
    So_hieu_QTKT = models.CharField(max_length= 300)
    So_quyet_dinh = models.CharField(max_length= 300)
    Ten_quy_trinh = models.TextField(max_length= 300)
    So_buoc = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.Ten_quy_trinh

class Buoc_quy_trinh(models.Model):
    Ten_quy_trinh = models.ForeignKey(Quy_trinh, on_delete=models.PROTECT)
    Ma_buoc_QT = models.CharField(max_length=50)
    Noi_dung_buoc = models.TextField(max_length= 300)
    Chi_so_an_toan = models.CharField(max_length=1, null=True, blank= True)
    def __str__(self):
        return self.Ten_quy_trinh
    
# # class Quy_trinh_giam_sat(models.Model):
# #     id_ten_quy_trinh=models.ForeignKey(Quy_trinh, on_delete=models.PROTECT, null = True,blank=True)
# #     So_buoc = models.IntegerField(default=0)
# #     Ngay_co_hieu_luc = models.DateField ()
# #     class Meta:
# #         ordering = ('-Ngay_co_hieu_luc',)
# #     def __str__(self) -> str:
# #         return self.Ten_quy_trinh
    
class Quy_trinh_giam_sat(models.Model):
    Nhan_vien_giam_sat = models.ForeignKey(Nhan_vien, on_delete=models.PROTECT)
    ID_Nhan_vien_duoc_giam_sat = models.CharField(max_length=300)
    Ten_quy_trinh = models.ForeignKey(Quy_trinh, on_delete=models.PROTECT)
    Kq_gs = models.TextField(max_length=9999)
    Ngay_giam_sat = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-Ngay_giam_sat',)
    def __id__(self):
        return self.id
