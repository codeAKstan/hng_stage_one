from django.urls import path
from .views import classify_number

urlpatterns = [
    path('classify-number/', classify_number, name='classify_number'),
    path('classify-number/<str:number>/', classify_number, name='classify_number'),
    path('classify-number/<int:number>/', classify_number, name='classify_number'),
]