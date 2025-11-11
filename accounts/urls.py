from django.urls import path
from . import views

urlpatterns = [
    path('submit_login/', views.submit_login, name='submit_login'),
]
