from django.urls import path
from . import views

urlpatterns = [
    path('', views.lotto_index, name='lotto_index'), # 메인 페이지
    path('purchase/', views.purchase_lotto, name='purchase_lotto'), # 구매 로직
]