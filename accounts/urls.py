from django.urls import path
from . import views

urlpatterns = [path("get-access-token", views.get_access_token)]
