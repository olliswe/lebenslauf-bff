from django.urls import path, include
from . import views


urlpatterns = [
    path("me", views.MeView.as_view()),
    path("get-access-token", views.get_access_token),
]
