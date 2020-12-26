from django.urls import path
from .views import dakhl, kharg
urlpatterns = [
    path('dakhl',dakhl),
    path('kharg',kharg)
]