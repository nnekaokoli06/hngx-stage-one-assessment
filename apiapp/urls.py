from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_jsondata, name='get_jsondata'),
]
