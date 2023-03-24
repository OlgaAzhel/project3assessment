from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishes_index, name='index'),
    path('index/<int:pk>/delete/', views.WishDelete.as_view(), name='wishes_delete'),
]