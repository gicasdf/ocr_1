from django.urls import path
from aiModel1 import views

urlpatterns = [
    path('admin/process_photos/', views.process_photos, name='process_photos'),
]
