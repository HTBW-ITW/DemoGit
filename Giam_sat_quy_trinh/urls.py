from django.urls import path
from Giam_sat_quy_trinh.views import *

app_name = 'Giam_sat_quy_trinh'
urlpatterns = [
    path('trang-chu', trang_chu, name= 'trang_chu'),
    path('master', master, name= 'master'),
    path('giam-sat-quy-trinh', giam_sat_quy_trinh, name= 'giam_sat_quy_trinh'),
    path('mau-giam-sat-<int:id_Ten_quy_trinh>/', form_quy_trinh, name= 'form_quy_trinh'),
]
