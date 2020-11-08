from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("", include(router.urls)),
    path("me", views.MeView.as_view()),
    path("get-access-token", views.get_access_token),
]
