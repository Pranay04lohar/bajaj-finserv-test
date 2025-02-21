from django.urls import path
from .views import process_data, get_operation_code

urlpatterns = [
    path('bfhl', process_data),  # Handles /bfhl (POST)
    path('bfhl/', process_data),  # Handles /bfhl/ (POST)
    path('bfhl', get_operation_code),  # Handles /bfhl (GET)
    path('bfhl/', get_operation_code),  # Handles /bfhl/ (GET)
]