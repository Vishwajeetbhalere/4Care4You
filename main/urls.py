# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SCAI/', views.SCAI, name='SCAI'),
    path('ISPIN/', views.ISPIN, name='ISPIN'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('usecase/', views.usecase, name='usecase'),
    path('contactus/', views.contact_view, name='contactus'),
]
