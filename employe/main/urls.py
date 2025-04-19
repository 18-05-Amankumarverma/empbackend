from django.urls import path
from . import views

urlpatterns = [
    path('api/get',views.home,name='home'),
    path('api/post',views.api,name='api'),
]