from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("me/cv", views.MyCV.as_view()),
    path("show-template", views.show_cv_template),
    path("dl-template", views.download_cv_template),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
