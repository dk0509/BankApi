from django.urls import path
from . import views

urlpatterns = [
     path('banks/', views.bank_list, name='bank-list'),
    path('branches/<str:ifsc>/', views.branch_detail, name='branch-detail'),
]