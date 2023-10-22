from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import select_account, get_user_accounts


urlpatterns = [
    path('users/select_account/', select_account, name="select_account"),
    path('users/accounts/', get_user_accounts, name="get_account"),
]
