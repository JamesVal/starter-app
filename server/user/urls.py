from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import select_account


urlpatterns = [
    path('users/select_account', select_account, name="select_account"),
]
