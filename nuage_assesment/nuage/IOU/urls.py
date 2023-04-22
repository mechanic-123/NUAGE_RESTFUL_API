from django.urls import path, include
from .views import create_user, create_iou, get_users

urlpatterns = [
    path("add/", create_user, name="create_user"),
    path("iou/", create_iou, name="create_iou"),
    path("users/", get_users, name="get_users"),
]
