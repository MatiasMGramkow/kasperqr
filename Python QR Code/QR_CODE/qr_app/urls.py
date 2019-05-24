from django.urls import path

from . import views

app_name = "qr_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('new_qr_web/', views.new_qr_web, name='new_qr_web')
]