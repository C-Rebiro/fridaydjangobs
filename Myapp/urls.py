from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('category/', views.category, name='my_category'),
    path('work/', views.work, name='my_work')
]