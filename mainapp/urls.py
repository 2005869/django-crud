from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.CreateData.as_view(), name='create'),
    path('read/', views.ReadData.as_view(), name='read'),
    path('update/<int:pk>', views.UpdateData.as_view(), name='update'),
]
