from django.urls import path
from . import views


urlpatterns = [path("me/cv", views.MyCV.as_view())]
