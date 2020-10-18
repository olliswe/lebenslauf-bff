from django.contrib import admin
from .models import CV

admin.site.register(CV)

admin.site.site_header = "Lebenslauf"
