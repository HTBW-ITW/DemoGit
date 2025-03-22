from django.db import models
from django.utils import *
# Create your models here.
class Khoi(models.Model):
    phan_loai_khoi = models.CharField(max_length=50)

class Khoa(models.Model):
    khoi = models.ForeignKey(Khoi, on_delete=models.PROTECT)
    khoa = models.CharField(max_length= 200)
    def __str__(self) -> str:
        return self.khoa  

class Nhan_vien(models.Model):
    khoa_NV = models.ForeignKey(Khoa, on_delete=models.PROTECT)
    ten_nhan_vien = models.CharField(max_length= 300)
    ma_nhan_vien = models.CharField(max_length= 10)
    email = models.EmailField(max_length=254)
    mat_khau = models.CharField(max_length=250, null=True, blank=True)
    hinh_anh = models.ImageField(default='nv1.jpg',null = True,blank=True, upload_to='images/')
    def __str__(self) -> str:
        return self.ma_nhan_vien